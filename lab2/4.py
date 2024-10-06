import time, tracemalloc
def binary_search(a, s):
    lw = 0
    hg = len(a) - 1
    while lw <= hg:
        mid = (lw + hg) // 2
        if s == a[mid]:
            return mid
        elif s > a[mid]:
            lw = mid + 1
        else:
            hg = mid - 1
    return -1
def main():
    tracemalloc.start()
    t_start = time.perf_counter()
    with open("input") as f:
        n = int(f.readline())
        a = list(map(int, f.readline().split()))
        k = int(f.readline())
        b = list(map(int, f.readline().split()))
    lst = []
    for i in range(k):
        if time.perf_counter() - t_start > 2:
            lst = ["-1"] * k
            break
        lst.append(binary_search(a, b[i]))
    res = " ".join(map(str, lst))
    with open("output", 'w') as w:
        w.write(res)
    print("Время работы: %s секунд" % (time.perf_counter() - t_start))
    print("Max memory ", tracemalloc.get_traced_memory()[1] / 2 ** 20, "mb")
    tracemalloc.stop()
if __name__ == "__main__":
    main()