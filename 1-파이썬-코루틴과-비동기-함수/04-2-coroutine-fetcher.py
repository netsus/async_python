import aiohttp
import time
import asyncio as ac


async def fetcher(sess, url):
    # async response = sess.get(url) # 이거 왜 에러나지?
    async with sess.get(url) as response:
        return await response.text()


async def main():
    urls = ["https://naver.com","https://google.com","https://instagram.com"]

    async with aiohttp.ClientSession() as sess:
        result = await ac.gather(*[fetcher(sess, url) for url in urls])
        print(result)

if __name__ == "__main__":
    start = time.time()
    ac.run(main())
    take = time.time() - start
    print(f"총 {take} 소요")
