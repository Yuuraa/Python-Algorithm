def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]


def union_find(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b


v, e = map(int, input().split())
parent = [i for i in range(v + 1)]

cycle = False
for i in range(e):
    v1, v2 = map(int, input().split())
    if find_parent(parent, v1) == find_parent(parent, v2):
        cycle = True
        break
    else:
        union_find(parent, v1, v2)

if cycle:
    print("사이클이 발생했습니다")
else:
    print("사이클이 없습니다")