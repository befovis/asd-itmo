import time, tracemalloc
def search_max_subarray(lst):
    frst_ind = 0
    lst_ind = 0
    sm = 0
    mx_sum = -10**10
    bl = False
    for i in range(len(lst)):
        if sm > 0 and bl:
            frst_ind = i-1
            bl = False
            sm += lst[i]
        if mx_sum < sm:
            mx_sum = sm
            lst_ind = i
        if sm < 0:
            bl = True
            sm = 0
    if frst_ind > lst_ind:
        frst_ind = lst_ind
    return lst[frst_ind:lst_ind+1]
tracemalloc.start()
t_start = time.perf_counter()
f = open("input.txt")
n = int(f.readline())
mas = [int(el) for el in f.readline().split()]
f.close()
str_lst = list(map(str, search_max_subarray(mas)))
res = " ".join(str_lst)
w = open("output.txt", 'w')
w.write(res)
w.close()
print("Время работы: %s секунд " % (time.perf_counter() - t_start))
print("Max memory ", tracemalloc.get_traced_memory()[1] / 2 ** 20, "mb")
tracemalloc.stop()
