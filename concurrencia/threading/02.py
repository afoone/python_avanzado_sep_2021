import time
import threading
import logging

logging.basicConfig(level=logging.DEBUG, format='[%(levelname)s] (%(threadName)-10s) %(message)s')

start = time.perf_counter()


def action(callback):
    logging.debug("iniciando")
    time.sleep(3)
    callback()
    logging.debug("finalizando")


def reacciona():
    print("he reaccionado")


t = threading.Thread(target=action, args=(reacciona,))
t.start()

t.join()

print("Terminado en ", time.perf_counter()-start)
