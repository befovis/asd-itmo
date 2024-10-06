def linear_search(mas, v):
    ind = []
    for i in range(len(mas)):
        if mas[i] == v:
            ind.append(i)
    if len(ind) > 0:
        return ind
    return [-1]

import time, tracemalloc
tracemalloc.start()
t_start = time.perf_counter()
f = open("input.txt")
mas = [el for el in f.readline().split()]
v = f.readline()
f.close()
str_lst = list(map(str, linear_search(mas, v)))
res = ", ".join(str_lst)
w = open("output.txt", 'w')
w.write(res)
w.close()
print("Время работы: %s секунд " % (time.perf_counter() - t_start))
print("Max memory ", tracemalloc.get_traced_memory()[1] / 2 ** 20, "mb")
tracemalloc.stop()





