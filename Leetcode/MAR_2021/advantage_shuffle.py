def advantage_shuffle(a, b):
    assert(len(a) == len(b))
    ans = [-1 for _ in range(len(a))]
    a.sort()
    b_sorted= sorted([(val, i) for i, val in enumerate(b)], key=lambda x: x[0])

    i, j = 0, 0
    added_ids = []
    while i < len(a) and j < len(b):
        if a[i] > b_sorted[j][0]:
            ans[b_sorted[j][1]] = a[i]
            added_ids.append(i)
            j += 1
        i += 1

    not_added = [idx for idx in range(len(a)) if idx not in added_ids]
    unfilled_ids = [idx for idx, val in enumerate(ans) if val == -1]
    assert(len(not_added) == len(unfilled_ids))
    for k in range(len(not_added)):
        ans[unfilled_ids[k]] = a[not_added[k]]
    
    # print(ans)
    return ans


if __name__ == "__main__":
    assert(advantage_shuffle([5621,1743,5532,3549,9581],[913,9787,4121,5039,1481]) == [1743,9581,5532,5621,3549])
    assert(advantage_shuffle([2,7,11,15], [1,10,4,11]) == [2,11,7,15])
    assert(advantage_shuffle([12,24,8,32], [13,25,32,11]) == [24,32,8,12])
    
    print("All examples passed")