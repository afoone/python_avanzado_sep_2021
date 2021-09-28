import time
import multiprocessing

start = time.perf_counter()


def dormir(seconds):
    print(f'durmiendo {seconds} segundo(s)')
    time.sleep(seconds)
    print(f'He terminado de dormir durante {seconds} segundo(s)')


procesos = []

for i in range(10):
    p = multiprocessing.Process(target=dormir, args=(i,))
    procesos.append(p)
    p.start()

for p in procesos:
    p.join()

# p1 = multiprocessing.Process(target=dormir)
# p2 = multiprocessing.Process(target=dormir)
#
# p1.start()
# p2.start()
#
# p1.join()
# p2.join()


print("Hemos terminado", time.perf_counter() - start)
