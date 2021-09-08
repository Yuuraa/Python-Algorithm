n = int(input())

explorers = list(map(int, input().split()))
explorers.sort()

n_groups, n_mems, min_req = 0, 0, explorers[0]
for e in explorers:
    if n_mems >= min_req:
        n_mems = 0
        n_groups += 1
    if e > min_req: min_req = e
    n_mems += 1

print(n_groups)