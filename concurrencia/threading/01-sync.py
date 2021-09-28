import time
import threading
import logging

logging.basicConfig(level=logging.DEBUG, format='[%(levelname)s] (%(threadName)-10s) %(message)s')

start = time.perf_counter()


def dormir(seconds: int) -> None:
    # print(f'durmiendo {seconds} segundo')
    logging.debug("iniciando")
    time.sleep(seconds)
    # print(f'Soy {threading.currentThread().getName()} y he terminado de dormir {seconds} segundos')
    logging.debug("finalizando")




threads = []
for i in range(10):
    threads.append(threading.Thread(target=dormir, args=(i,), name=f'Servicio numero {i}'))
    threads[i].start()

for t in threads:
    t.join()


print("Terminado en ", time.perf_counter()-start)
