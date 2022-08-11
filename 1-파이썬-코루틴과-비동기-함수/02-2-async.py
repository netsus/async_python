import time
import asyncio

async def deliver(meal,t):
    print(f"{meal} 시작",end=' ')
    await asyncio.sleep(t)
    print(f"{meal} 끝, {t} 소요")
    return t

async def main():
    await asyncio.gather(
        deliver("A", 4),
        deliver("B", 3),
        deliver("C", 2),
    )


if __name__=="__main__":
    start = time.time()
    asyncio.run(main())
    take=time.time()-start
    print(f"총 {take} 소요")


