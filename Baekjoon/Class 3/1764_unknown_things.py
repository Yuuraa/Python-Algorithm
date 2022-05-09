import sys


n, m = map(int, sys.stdin.readline().split())
unseen_list, unheard_list, cnt = [], [], 0

for _ in range(n):
    unseen_list.append(sys.stdin.readline().rstrip("\n"))
for _ in range(m):
    unheard_list.append(sys.stdin.readline().rstrip("\n"))

tot_list = set(unseen_list) & set(unheard_list)

print(len(tot_list))
for p in sorted(tot_list):
    print(p)