
arr = list(range(1000))  # [0, 1, 2, ..., 999] (sorted)

def linear_search(a, x):
    for i, val in enumerate(a):
        if val == x:
            return i
    return -1

def binary_search(a, x):
    lo, hi = 0, len(a) - 1
    while lo <= hi:
        mid = (lo + hi) // 2
        if a[mid] == x:
            return mid
        elif a[mid] < x:
            lo = mid + 1
        else:
            hi = mid - 1
    return -1

hashset = set(arr)
def hash_lookup(s, x):
    return x in s  # True/False


targets = [42, 1234]  

for t in targets:
    i_lin = linear_search(arr, t)
    i_bin = binary_search(arr, t)
    in_set = hash_lookup(hashset, t)
    print(f"Target {t}:")
    print(f"  Linear search -> index {i_lin}")
    print(f"  Binary search -> index {i_bin}")
    print(f"  Hash lookup   -> {'found' if in_set else 'not found'}")