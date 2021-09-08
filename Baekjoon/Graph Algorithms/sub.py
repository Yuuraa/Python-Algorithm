import sys
import heapq

n = int(input())
num_microbe = list(map(int, input().split()))
microbe_price = list(map(int, input().split()))
min_incomes = [p for p in microbe_price]

edges = []
for i in range(n):
    heapq.heappush(edges, (microbe_price[i], 0, i+1))
for i in range(n):
    price = list(map(int, sys.stdin.readline().split()))
    for j, p in enumerate(price):
        min_incomes[j] = min(min_incomes[j], p)
        heapq.heappush(edges, (p, i+1, j+1))

parent = [i for i in range(n+1)]

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

count, initial_price = 0, 0

while edges and count < n:
    price, a, b = heapq.heappop(edges)
    if find_parent(parent, a) == find_parent(parent, b):
        continue
    else:
        union_find(parent, a, b)
        count += 1
        initial_price += price

num_microbe = [num - 1 for num in num_microbe]
total_price = initial_price + sum([p*num for p, num in zip(min_incomes, num_microbe)])

print(total_price)
