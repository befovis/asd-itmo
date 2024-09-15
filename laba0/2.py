import time, tracemalloc
tracemalloc.start()
t_start = time.perf_counter()
from functools import lru_cache
@lru_cache()
def calc_fib(n):
    if (n <= 1):
        return n
    return calc_fib(n - 1) + calc_fib(n - 2)
f = open("input.txt")
n = int(f.readline())
f.close()
w = open('output.txt', 'w')
w.write(str(calc_fib(n)))
w.close
print("Время работы: %s секунд " % (time.perf_counter() - t_start))
print("Max memory ", tracemalloc.get_traced_memory()[1] / 2 ** 20, "mb")
tracemalloc.stop()