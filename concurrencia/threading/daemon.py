import time
import threading
import logging

logging.basicConfig(level=logging.DEBUG, format='[%(levelname)s] (%(threadName)-10s) %(message)s')

start = time.perf_counter()


def dormir() -> None:
    for _ in range(10):
        time.sleep(1)
        print("hola")


t = threading.Thread(target=dormir)
t.setDaemon(True)
t.start()
time.sleep(5)
print("Terminado en ", time.perf_counter()-start)
