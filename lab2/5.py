import time, tracemalloc
def count_occurrences(arr, left, right, element):
    count = 0
    for i in range(left, right + 1):
        if arr[i] == element:
            count += 1
    return count
def majority_element_rec(arr, left, right):
    if left == right:
        return arr[left]
    mid = (left + right) // 2
    left_majority = majority_element_rec(arr, left, mid)
    right_majority = majority_element_rec(arr, mid + 1, right)
    if left_majority == right_majority:
        return left_majority
    left_count = count_occurrences(arr, left, right, left_majority)
    right_count = count_occurrences(arr, left, right, right_majority)
    return left_majority if left_count > right_count else right_majority
def has_majority_element(arr):
    n = len(arr)
    candidate = majority_element_rec(arr, 0, n - 1)
    count = count_occurrences(arr, 0, n - 1, candidate)
    if count > n // 2:
        return 1
    return 0
if __name__ == "__main__":
    with open("scr/input", "r") as file:
        n = int(file.readline())
        arr = list(map(int, file.readline().split()))
    result = has_majority_element(arr)
    with open("scr/output", "w") as file:
        file.write(str(result) + "\n")
tracemalloc.start()
t_start = time.perf_counter()
print("Время работы: %s секунд " % (time.perf_counter() - t_start))
print("Max memory ", tracemalloc.get_traced_memory()[1] / 2 ** 20, "mb")
tracemalloc.stop()