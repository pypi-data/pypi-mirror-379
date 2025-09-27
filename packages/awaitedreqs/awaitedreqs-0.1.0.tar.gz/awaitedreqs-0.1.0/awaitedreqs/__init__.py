import aiohttp
import asyncio
import ssl
import time
from datetime import timedelta
from http.cookies import SimpleCookie
from urllib.parse import urljoin
import chardet
import io

# Utility: Case insensitive dict for headers
class CaseInsensitiveDict(dict):
    def __getitem__(self, key): return super().__getitem__(key.lower())
    def __setitem__(self, key, value): super().__setitem__(key.lower(), value)
    def __contains__(self, key): return super().__contains__(key.lower())
    def get(self, key, default=None): return super().get(key.lower(), default)

# Minimal PreparedRequest mimic for Response.request property
class PreparedRequest:
    def __init__(self, method: str, url: str):
        self.method = method
        self.url = url

# Response class mimicking requests.Response async style
class AsyncResponse:
    def __init__(self, aiohttp_response: aiohttp.ClientResponse, content: bytes, elapsed: timedelta,
                 history=None):
        self._resp = aiohttp_response
        self._content = content
        self.elapsed = elapsed
        self.history = history or []
        self.status_code = aiohttp_response.status
        self.reason = aiohttp_response.reason
        self.headers = CaseInsensitiveDict(aiohttp_response.headers)
        self.cookies = aiohttp_response.cookies
        self.url = str(aiohttp_response.url)
        self.encoding = None
        self._apparent_encoding = None
        self._content_consumed = content is not None
        self.request = PreparedRequest(aiohttp_response.method, self.url)
        self._streaming = content is None
        self._raw = aiohttp_response.content if self._streaming else io.BytesIO(content)

    @property
    def apparent_encoding(self):
        if self._apparent_encoding:
            return self._apparent_encoding
        if self._content:
            result = chardet.detect(self._content)
            self._apparent_encoding = result["encoding"]
            return self._apparent_encoding
        return None

    def close(self):
        if not self._resp.closed:
            self._resp.close()

    @property
    def content(self):
        if self._content_consumed:
            return self._content
        raise RuntimeError("Content not read yet (stream=True). Use iter_content/read.")

    @property
    def text(self):
        enc = self.encoding or self.apparent_encoding or 'utf-8'
        return self._content.decode(enc, errors='replace') if self._content else ''

    @property
    def ok(self):
        return 200 <= self.status_code < 400

    @property
    def is_redirect(self):
        return 'location' in self.headers and self.status_code in (301, 302, 303, 307, 308)

    @property
    def is_permanent_redirect(self):
        return self.status_code in (301, 308)

    def raise_for_status(self):
        if not self.ok:
            raise aiohttp.ClientResponseError(
                self._resp.request_info,
                self._resp.history,
                status=self.status_code,
                message=self.reason,
                headers=self.headers)

    async def json(self, **kwargs):
        return await self._resp.json(**kwargs)

    def iter_content(self, chunk_size=1, decode_unicode=False):
        if not self._streaming:
            def gen():
                data = self._content
                if decode_unicode:
                    text = data.decode(self.encoding or self.apparent_encoding or 'utf-8', errors='replace')
                    for i in range(0, len(text), chunk_size):
                        yield text[i:i+chunk_size]
                else:
                    for i in range(0, len(data), chunk_size):
                        yield data[i:i+chunk_size]
            return gen()
        else:
            async def aiter():
                while True:
                    chunk = await self._raw.read(chunk_size)
                    if not chunk:
                        break
                    if decode_unicode:
                        yield chunk.decode(self.encoding or self.apparent_encoding or 'utf-8', errors='replace')
                    else:
                        yield chunk
            return aiter()

    def iter_lines(self, chunk_size=512, decode_unicode=False, delimiter=None):
        if not self._streaming:
            def gen():
                data = self._content
                text = data.decode(self.encoding or self.apparent_encoding or 'utf-8', errors='replace')
                lines = text.split(delimiter or '\n')
                for line in lines:
                    yield line
            return gen()
        else:
            async def aiter():
                buffer = ''
                async for chunk in self._raw.iter_chunked(chunk_size):
                    text = chunk.decode(self.encoding or self.apparent_encoding or 'utf-8', errors='replace')
                    buffer += text
                    while True:
                        if delimiter is None:
                            if '\n' not in buffer:
                                break
                            line, buffer = buffer.split('\n', 1)
                            yield line
                        else:
                            if delimiter not in buffer:
                                break
                            line, buffer = buffer.split(delimiter, 1)
                            yield line
                if buffer:
                    yield buffer
            return aiter()

    @property
    def links(self):
        link_header = self.headers.get('link', '')
        links = {}
        for val in link_header.split(','):
            parts = val.split(';')
            if len(parts) < 2:
                continue
            url_part = parts[0].strip()[1:-1]
            rel_part = None
            for p in parts[1:]:
                if p.strip().startswith('rel='):
                    rel_part = p.strip()[4:].strip('\"')
            if rel_part:
                links[rel_part] = url_part
        return links

    @property
    def next(self):
        if self.history:
            return self.history[-1].request
        return None

    @property
    def raw(self):
        return self._raw

async def request(method: str, url: str, params=None, data=None, json=None, headers=None,
                  cookies=None, files=None, auth=None, timeout=None, allow_redirects=True,
                  proxies=None, verify=True, stream=False, cert=None, history=None):
    timeout_obj = aiohttp.ClientTimeout(total=timeout if isinstance(timeout, (int, float)) else None)
    connector_params = {}

    if not verify:
        ssl_context = ssl.create_default_context()
        ssl_context.check_hostname = False
        ssl_context.verify_mode = ssl.CERT_NONE
        connector_params['ssl'] = ssl_context
    elif isinstance(verify, str):
        ssl_context = ssl.create_default_context(cafile=verify)
        connector_params['ssl'] = ssl_context

    if cert is not None:
        if isinstance(cert, tuple):
            connector_params['cert_file'] = cert[0]
            connector_params['key_file'] = cert[1]
        elif isinstance(cert, str):
            connector_params['cert_file'] = cert

    send_data = data
    if files:
        form = aiohttp.FormData()
        if data and isinstance(data, dict):
            for k, v in data.items():
                form.add_field(k, v)
        for k, v in files.items():
            if isinstance(v, tuple):
                filename, fileobj = v[:2]
                content_type = v[2] if len(v) > 2 else None
                custom_headers = v[3] if len(v) > 3 else None
                form.add_field(k, fileobj, filename=filename,
                               content_type=content_type, headers=custom_headers)
            else:
                form.add_field(k, v)
        send_data = form

    import time as _time
    start = _time.monotonic()

    async with aiohttp.ClientSession(cookies=cookies,
                                     auth=aiohttp.BasicAuth(*auth) if isinstance(auth, tuple) and len(auth) == 2 else None,
                                     **connector_params) as session:
        req = session.request(
            method,
            url,
            params=params,
            data=send_data,
            json=json,
            headers=headers,
            timeout=timeout_obj,
            allow_redirects=allow_redirects
        )
        async with req as resp:
            elapsed = timedelta(seconds=_time.monotonic() - start)
            if stream:
                return AsyncResponse(resp, None, elapsed, history=history)
            content = await resp.read()
            return AsyncResponse(resp, content, elapsed, history=history)

async def get(url, **kwargs):
    return await request('GET', url, **kwargs)

async def post(url, **kwargs):
    return await request('POST', url, **kwargs)

async def put(url, **kwargs):
    return await request('PUT', url, **kwargs)

async def delete(url, **kwargs):
    return await request('DELETE', url, **kwargs)

async def patch(url, **kwargs):
    return await request('PATCH', url, **kwargs)

async def head(url, **kwargs):
    return await request('HEAD', url, **kwargs)

async def options(url, **kwargs):
    return await request('OPTIONS', url, **kwargs)

class Session:
    def __init__(self, **kwargs):
        self._client_session = None
        self._session_args = kwargs

    async def __aenter__(self):
        self._client_session = aiohttp.ClientSession(**self._session_args)
        return self

    async def __aexit__(self, exc_type, exc, tb):
        if self._client_session:
            await self._client_session.close()

    async def close(self):
        if self._client_session:
            await self._client_session.close()

    async def request(self, method, url, **kwargs):
        if self._client_session is None:
            self._client_session = aiohttp.ClientSession(**self._session_args)
        import time as _time
        start = _time.monotonic()
        async with self._client_session.request(method, url, **kwargs) as resp:
            elapsed = timedelta(seconds=_time.monotonic() - start)
            content = await resp.read()
            return AsyncResponse(resp, content, elapsed)

    async def get(self, url, **kwargs):
        return await self.request("GET", url, **kwargs)

    async def post(self, url, **kwargs):
        return await self.request("POST", url, **kwargs)

    async def put(self, url, **kwargs):
        return await self.request("PUT", url, **kwargs)

    async def delete(self, url, **kwargs):
        return await self.request("DELETE", url, **kwargs)

    async def patch(self, url, **kwargs):
        return await self.request("PATCH", url, **kwargs)

    async def head(self, url, **kwargs):
        return await self.request("HEAD", url, **kwargs)

    async def options(self, url, **kwargs):
        return await self.request("OPTIONS", url, **kwargs)
