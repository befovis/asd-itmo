import time, tracemalloc
def binary_search(a, s):
    lw = 0
    hg = len(a)-1
    mid = 0
    while lw <= hg:
        mid = (lw + hg)//2
    if s == a[mid]:
        return mid
    if s > a[mid]:
        lw = mid + 1
    if s < a[mid]:
        hg = mid - 1
    return -1
tracemalloc.start()
t_start = time.perf_counter()
f = open("input.txt")
n = int(f.readline())
a = [int(el) for el in f.readline().split()]
k = int(f.readline())
b = [int(el) for el in f.readline().split()]
f.close()
lst = []
for i in range(k):
    lst.append(binary_search(a, b[i]))
str_lst = list(map(str, lst))
res = " ".join(str_lst)
w = open("output.txt", 'w')
w.write(res)
w.close()
print("Время работы: %s секунд " % (time.perf_counter() - t_start))
print("Max memory ", tracemalloc.get_traced_memory()[1] / 2 ** 20, "mb")
tracemalloc.stop()
