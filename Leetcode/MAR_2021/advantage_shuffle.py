def advantage_shuffle(a, b):
    perm_a = [-1 for _ in range(len(a))]
    a.sort()
    sorted_b = sorted([(val, i) for i, val in enumerate(b)], key=lambda x: x[0])
    
    i, j = 0, 0
    added = []
    while i < len(a) and j < len(b):
        if a[i] > sorted_b[j][0]:
            perm_a[sorted_b[j][1]] = a[i]
            added.append[i]
            j += 1
        i += 1

    k = 0
    for i in range(len(a)):
        if i in added:
            continue
        else:
            