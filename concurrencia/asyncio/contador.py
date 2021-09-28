import asyncio
import time

start = time.perf_counter()


async def count():
    print("uno")
    await asyncio.sleep(1)
    print("dos")


async def arranca_procesos():
    await asyncio.gather(count(), count(), count())

asyncio.run(arranca_procesos())


print(time.perf_counter()-start)
