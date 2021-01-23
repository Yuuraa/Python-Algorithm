array = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]

for i in range(len(array)):
    min_id = i
    for j in range(i+1, len(array)):
        if array[j] < array[min_id]:
            min_id = j
    array[i], array[min_id] = array[min_id], array[i]