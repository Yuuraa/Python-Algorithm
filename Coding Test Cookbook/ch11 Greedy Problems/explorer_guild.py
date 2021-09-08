n = int(input())

fearness = list(map(int, input().split()))
fearness.sort()
ans = 0

curr_mem, max_val = 0, 1

for f in fearness:
    curr_mem += 1
    max_val = f
    if curr_mem >= max_val:
        curr_mem = 0
        ans += 1

print(ans)