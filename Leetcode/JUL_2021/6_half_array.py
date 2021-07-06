from collections import Counter

def min_set_size(arr):
    size = len(arr)
    count_elems = Counter(arr)
    count_elems = sorted([(i, v) for i, v in count_elems.items()], key=lambda x: -x[1])
    ans, removed = 0, 0
    for _, cnt in count_elems:
        ans += 1
        removed += cnt
        if removed >= size / 2:
            break
    return ans
