from setuptools import setup, find_packages

long_description = """
# aiohttprequests

An async requests-like HTTP client built on aiohttp with requests-compatible API.

## Installation

pip install aiohttprequests

text

## Usage

import aiohttprequests as requests
import asyncio

async def main():
# Simple GET
response = await requests.get('https://httpbin.org/get')
print(response.content)
print(response.text)
data = await response.json()
print(data)

text
# Using Session for persistent connection and cookies
async with requests.Session() as session:
    await session.get('https://httpbin.org/cookies/set/sessioncookie/123456789')
    r = await session.get('https://httpbin.org/cookies')
    print(await r.text)
asyncio.run(main())

text

## Features

- Fully async API, drop-in replacement for `requests` with `async/await`.
- Supports all standard HTTP methods: `get`, `post`, `put`, `delete`, etc.
- Session support with cookie persistence.
- Response object mimics `requests.Response`.
- Supports streaming, file uploads, JSON, timeout, headers, auth, and more.

## Notes

- Must call all methods with `await` inside async functions.
- Requires Python 3.7+ and aiohttp installed.

## License

MIT License
"""

setup(
    name='awaitedreqs',
    version='0.1.1',
    description='Async requests-like HTTP client built on aiohttp with requests-compatible API',
    long_description=long_description,
    long_description_content_type='text/markdown',
    author='kokodev',
    author_email='koko@kokodev.cc',
    url='https://github.com/kokofixcomputers/awaitedreqs',
    packages=find_packages(),
    install_requires=[
        'aiohttp>=3.8.0',
        'chardet',
    ],
    python_requires='>=3.7',
    classifiers=[
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Operating System :: OS Independent',
        'License :: OSI Approved :: MIT License',
        'Intended Audience :: Developers',
        'Topic :: Internet :: WWW/HTTP :: HTTP Servers',
    ],
    keywords='async http requests aiohttp http-client',
)