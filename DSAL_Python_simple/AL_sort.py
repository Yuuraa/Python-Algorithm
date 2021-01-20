import random
import argparse

# Define sorting methods
def bubble_sort(data_list):
    sortDone = True
    for j in range(len(data_list) -1 - i):
        if data_list[j] > data_list[j+1]:
            data_list[j], data_list[j+1] = data_list[j+1], data_list[j] # Swap
            sortDone = False # Not sorted yet
        if sortDone: break
    return data_list

def quick_sort(data_list):
    if len(data_list) <= 1:
        return data_list
    pivot = data_list.pop(0)
    left = []
    right = []
    for data in data_list:
        if data < pivot:
            left.append(data)
        else:
            right.append(data)
    return quick_sort(left) + [pivot] + quick_sort(right)


    


if __name__ == '__main__':
    data_list = random.sample(range(100), 10)
    print('List before sorted:\n', data_list)

    # bubble_sort(data_list)
    # print('Sorted list:\n', data_list)

    quick_sorted = quick_sort(data_list)
    print('Sorted with quick sort:\n', quick_sorted)
