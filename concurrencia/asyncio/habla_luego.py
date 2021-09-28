import asyncio
import time


async def suma_tres(n):
    return n + 3


async def cuadrado(j):
    return await suma_tres(j*j)


async def cuadrados_mas_3():
    for i in range(10):
        res = await cuadrado(i)
        print(f'para el numero {i} su cuadrado mas tres es {res}')

asyncio.run(cuadrados_mas_3())
