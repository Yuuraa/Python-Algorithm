n = int(input())
component_list = list(map(int, input().split()))
component_list.sort()

m = int(input())
requested_list = list(map(int, input().split()))


def binary_search(array, target):
    start, end = 0, len(array) - 1
    while start <= end:
        mid = (start + end) // 2
        if array[mid] == target:
            return True
        elif array[mid] < target:
            start = mid + 1
        else:
            end = mid - 1
    return False

# Solve using binary search
for requested_num in requested_list:
    if binary_search(component_list, requested_num):
        print('yes', end=' ')
    else:
        print('no', end=' ')

# 내 생각: 굳이 binary search 쓰지 않고 in 을 써도 될듯 (책에서도 나온다)
print('Solution without binary search')
copmonent_set = set(component_list)
for requested_num in requested_list:
    if requested_num in copmonent_set:
        print('yes', end=' ')
    else:
        print('no', end=' ')