import time
import concurrent.futures

start = time.perf_counter()


def dormir(seconds):
    print(f'Durmiendo {5} segundos')
    time.sleep(5)
    print("Ya no duermo")
    return f'Terminado el proceso de {5} segundos'


with concurrent.futures.ThreadPoolExecutor(max_workers=5) as executor:
    res = executor.map(dormir, range(10))  # me da las respuestas directamente

    # for f in concurrent.futures.as_completed(res):
    #     print(f.result())
    for f in res:
        print(f)


print(time.perf_counter() - start)
