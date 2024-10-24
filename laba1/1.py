def insertion_sort(n, lst):
    for i in range(1, n):
        for j in range(i, 0, -1):
            if lst[j] < lst[j - 1]:
                lst[j], lst[j - 1] = lst[j - 1], lst[j]
            else:
                break
    return lst
import time, tracemalloc
tracemalloc.start()
t_start = time.perf_counter()
f = open("scr/input.txt")
n = int(f.readline())
mas = [int(el) for el in f.readline().split()]
f.close()
str_lst = list(map(str, insertion_sort(n, mas)))
res = " ".join(str_lst)
w = open("scr/output.txt", 'w')
w.write(res)
w.close()
print("Время работы: %s секунд " % (time.perf_counter() - t_start))
print("Max memory ", tracemalloc.get_traced_memory()[1] / 2 ** 20, "mb")
tracemalloc.stop()