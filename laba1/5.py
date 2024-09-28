import time, tracemalloc
def selection_sort(n, lst):
    for i in range(n-1):
        mn = lst[i]
        temp = i
        for j in range(i+1, n):
            if mn > lst[j]:
                mn = j
                temp = j
    if temp != i:
        lst[i], lst[temp] = lst[temp], lst[i]
    return lst
tracemalloc.start()
t_start = time.perf_counter()
f = open("input.txt")
n = int(f.readline())
mas = [int(el) for el in f.readline().split()]
f.close()
str_lst = list(map(str, selection_sort(n, mas)))
res = " ".join(str_lst)
w = open("output.txt", 'w')
w.write(res)
w.close()
print("Время работы: %s секунд " % (time.perf_counter() - t_start))
print("Max memory ", tracemalloc.get_traced_memory()[1] / 2 ** 20, "mb")
tracemalloc.stop()

