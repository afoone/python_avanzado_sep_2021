import threading
import time
import logging

logging.basicConfig(level=logging.DEBUG, format='%(threadName)-10s %(message)s')


def wait_for_event(event):
    """
    Espera un evento para ejecutarse
    :param event:
    :return:
    """
    logging.debug("esperando")
    event_is_set = event.wait(2)
    if event_is_set:
        logging.debug('event set %s', event_is_set)
    else:
        logging.debug('haciendo otras cosas')


e = threading.Event()
t1 = threading.Thread(name="waiting", target=wait_for_event, args=(e,))

t1.start()

time.sleep(4)
e.set()

t1.join()

logging.debug("Terminando la ejecucion.")

