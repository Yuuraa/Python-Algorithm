
import sys
import heapq

n = int(input())

people = []
for i in range(n):
    age, name = sys.stdin.readline().split()
    people.append((int(age), i, name))

people.sort(key=lambda x:(x[0], x[1]))
for age, _, name in people:
    print(age, name)