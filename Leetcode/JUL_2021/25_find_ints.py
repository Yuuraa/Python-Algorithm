# def find_integers(n):
#     if n < 3: return n + 1
#     i = 0
#     while 3 * (1 << (i+1)) <= n: 
#         i += 1
#     if i == 0: return n
    
#     print(1 << (i-1), min((1<<i), n-3*(1<<i) + 1))
#     return n+1 - ((1 << (i-1)) + min((1<<i), n+1-3*(1<<i)))

# print(find_integers(6)) # 5
# print(find_integers(7)) # 5
# print(find_integers(5)) # 5
# print(find_integers(11)) # 8

def print_ints(n):
    ans = []
    for i in range(n+1):
        if '11' in bin(i)[2:]:
            ans.append(i)
    print(ans)
    print(len(ans))

print_ints(64)
print_ints(128)
print_ints(32)
print_ints(16)

