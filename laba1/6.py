import time, tracemalloc
def bubble_sort(n, lst):
    for i in range(n-1):
        exc = 0
        for j in range(n - i - 1):
            if lst[j] > lst[j+1]:
                exc += 1
                lst[j], lst[j+1] = lst[j+1], lst[j]
        if exc == 0:
            break
    return lst
def proof(lst):
    for i in range(len(lst)-1):
        if not(int(lst[i]) <= int(lst[i+1])):
            return False
        return True
tracemalloc.start()
t_start = time.perf_counter()
f = open("scr/input.txt")
n = int(f.readline())
mas = [int(el) for el in f.readline().split()]
f.close()
str_lst = list(map(str, bubble_sort(n, mas)))
res = " ".join(str_lst)
w = open("scr/output.txt", 'w')
w.write(res)
w.close()
print("Время работы: %s секунд " % (time.perf_counter() - t_start))
print("Max memory ", tracemalloc.get_traced_memory()[1] / 2 ** 20, "mb")
print(proof(str_lst))
tracemalloc.stop()
