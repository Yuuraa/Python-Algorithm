def recursive_binary_search(start, end, array, target):
    if start >= end:
        return None
    
    mid = (start + end) // 2
    if array[mid] == target:
        return mid
    elif array[mid] < target:
        return recursive_binary_search(mid + 1, end, array, target)
    else:
        return recursive_binary_search(start, mid - 1, array, target)


def binary_search(array, target):
    start, end = 0, len(array) - 1

    while start <= end:
        mid = (start + end) // 2
        if array[mid] == target:
            return mid
        elif array[mid] < target:
            start = mid + 1
        else:
            end = mid - 1


if __name__ == "__main__":
    n, target = map(int, input('리스트 원소의 갯수와 타겟 넘버를 입력하세요: ').split())
    array = list(map(int, input('정렬된 리스트를 입력하세요: ').split()))

    # index = recursive_binary_search(0, n, array, target)
    index = binary_search(array, target)
    if index:
        print(f'원소 {target}의 위치는 {index + 1} 입니다.')
    else:
        print('찾으시는 원소가 리스트에 없습니다.')