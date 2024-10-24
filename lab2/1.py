import time, tracemalloc
def merge_sort(lst):
    ln = len(lst)//2
    mas1 = lst[:ln]
    mas2 = lst[ln:]
    if len(mas1) > 1:
         mas1 = merge_sort(mas1)
    if len(mas2) > 1:
        mas2 = merge_sort(mas2)
    return merge(mas1, mas2)
def merge(a, b):
    mas = []
    i = 0
    j = 0
    while i < len(a) and j < len(b):
        if a[i] <= b[j]:
            mas.append(a[i])
            i += 1
        else:
            mas.append(b[j])
            j += 1
    mas += a[i:] + b[j:]
    return mas
tracemalloc.start()
t_start = time.perf_counter()
f = open("scr/input")
n = int(f.readline())
mas = [int(el) for el in f.readline().split()]
f.close()
str_lst = list(map(str, merge_sort(mas)))
res = " ".join(str_lst)
w = open("scr/output", 'w')
w.write(res)
w.close()
print("Время работы: %s секунд " % (time.perf_counter() - t_start))
print("Max memory ", tracemalloc.get_traced_memory()[1] / 2 ** 20, "mb")
tracemalloc.stop()
