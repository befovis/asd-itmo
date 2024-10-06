import time, tracemalloc
def merge_and_count(arr, temp_arr, left, right):
    if left == right:
        return 0
    mid = (left + right) // 2
    inv_count = 0
    inv_count += merge_and_count(arr, temp_arr, left, mid)
    inv_count += merge_and_count(arr, temp_arr, mid + 1, right)
    inv_count += merge(arr, temp_arr, left, mid, right)
    return inv_count
def merge(arr, temp_arr, left, mid, right):
    i = left    # Начало левой части
    j = mid + 1 # Начало правой части
    k = left    # Индекс для временного массива
    inv_count = 0
    while i <= mid and j <= right:
        if arr[i] <= arr[j]:
            temp_arr[k] = arr[i]
            i += 1
        else:
            temp_arr[k] = arr[j]
            inv_count += (mid - i + 1)
            j += 1
        k += 1
    while i <= mid:
        temp_arr[k] = arr[i]
        i += 1
        k += 1

    while j <= right:
        temp_arr[k] = arr[j]
        j += 1
        k += 1

    for i in range(left, right + 1):
        arr[i] = temp_arr[i]

    return inv_count

def count_inversions(arr, n):
    temp_arr = [0] * n
    return merge_and_count(arr, temp_arr, 0, n - 1)

if __name__ == "__main__":
    with open("input", "r") as file:
        n = int(file.readline())
        arr = list(map(int, file.readline().split()))

    result = count_inversions(arr, n)

    with open("output", "w") as file:
        file.write(str(result) + "\n")
tracemalloc.start()
t_start = time.perf_counter()
print("Время работы: %s секунд " % (time.perf_counter() - t_start))
print("Max memory ", tracemalloc.get_traced_memory()[1] / 2 ** 20, "mb")
tracemalloc.stop()