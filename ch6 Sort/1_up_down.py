n = int(input())
sorted_list = []

for _ in range(n):
    sorted_list.append(int(input()))

sorted_list.sort(reverse=True)
for num in sorted_list:
    print(num, end=' ')