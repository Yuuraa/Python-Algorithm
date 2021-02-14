answers = []

def check_palindrome(input_str):
    left, right = 0, len(input_str) - 1
    while left < right:
        if input_str[left] != input_str[right]:
            return "no"
        else:
            left += 1
            right -= 1
    return "yes"


while True:
    input_str = input()
    if input_str == '0':
        break
    answers.append(check_palindrome(input_str))

for ans in answers:
    print(ans)