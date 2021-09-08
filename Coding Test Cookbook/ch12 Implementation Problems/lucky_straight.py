input_str = input()
n = len(input_str)

left_sum = sum(list(map(int, list(input_str[:n//2]))))
right_sum = sum(list(map(int, list(input_str[n//2:]))))

if left_sum == right_sum:
    print("LUCKY")
else:
    print("READY")
