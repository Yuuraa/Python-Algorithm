def gray_code(n):
    codes = [0]
    for i in range(n):
        codes = [0] + [num*2 + 1 for num in codes] + [num*2 for num in codes[::-1][:-1]]
    return codes

n = int(input())
print(gray_code(n))

# n을 구하기 전, n-1번째 gray code를 구하는 방식. 초기값은 0으로, bottom-up 방식으로 구현했다
# 
