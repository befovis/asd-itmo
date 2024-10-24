def swap(arr, i, j):
    arr[i], arr[j] = arr[j], arr[i]
def insertion_sort_desc(arr):
    for i in range(1, len(arr)):
        j = i
        while j > 0 and arr[j] > arr[j - 1]:
            swap(arr, j, j - 1)
            j -= 1
import time, tracemalloc
tracemalloc.start()
t_start = time.perf_counter()
with open('scr/input.txt', 'r') as f:
    n = int(f.readline())
    arr = list(map(int, f.readline().split()))
insertion_sort_desc(arr)
with open('scr/output.txt', 'w') as f:
    f.write(" ".join(map(str, arr)) + "\n")
print("Время работы: %s секунд " % (time.perf_counter() - t_start))
print("Max memory ", tracemalloc.get_traced_memory()[1] / 2 ** 20, "mb")
tracemalloc.stop()