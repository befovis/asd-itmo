def addition_bin(a, b):
    n = len(a)
    temp = 0
    res = ''
    for i in range(n-1, -1, -1):
        if int(a[i]) + int(b[i]) == 2:
            if temp == 0:
                res = '0' + res
            else:
                res = '1' + res
            temp = 1
        elif int(a[i]) + int(b[i]) == 1:
            if temp == 1:
                res = '0' + res
                temp = 1
            else:
                res = '1' + res
        else:
            if temp == 1:
                res = '1' + res
                temp = 0
            else:
                res = '0' + res
    if temp == 1:
        res = "1" + res
    return res
import time, tracemalloc
tracemalloc.start()
t_start = time.perf_counter()
f = open("scr/input.txt")
a, b = map(str, f.readline().split())
res = addition_bin(a, b)
w = open("scr/output.txt", 'w')
w.write(res)
w.close()
print("Время работы: %s секунд " % (time.perf_counter() - t_start))
print("Max memory ", tracemalloc.get_traced_memory()[1] / 2 ** 20, "mb")
tracemalloc.stop()