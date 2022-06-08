# asynchronous requests in python
import asyncio
import aiohttp
import time

async def fetchFromGoogle():
    url = 'https://www.google.com'
    session = aiohttp.ClientSession()
    resp = await session.get(url)
    async with open("file.txt", 'w') as file:
        await resp.content.read(256)
    await session.close()

async def main():
    print(time.strftime('%X'))
    await asyncio.gather(
        *[
            fetchFromGoogle() for _ in range(20)
        ]
        # above or below
        # await fetchFromGoogle(),
        # await fetchFromGoogle(),
        # await fetchFromGoogle(),
        # await fetchFromGoogle(),
        # await fetchFromGoogle(),
        # await fetchFromGoogle(),
        # await fetchFromGoogle(),
        # await fetchFromGoogle(),
        # await fetchFromGoogle()
    )
    print(time.strftime('%X'))

if __name__ == '__main__':
    asyncio.run(main())