input_str = input()
sorted_list = sorted(input_str)

idx = 0
while sorted_list[idx].isdigit():
    idx += 1

ordered_list = sorted_list[idx:] + sorted_list[:idx]


print(''.join(ordered_list))