import sys

n = int(input())
coords = []

for _ in range(n):
    a, b = map(int, sys.stdin.readline().split())
    coords.append((a, b))

coords.sort(key=lambda x: (x[0], x[1]))
for a, b in coords:
    print(a, b)
