s = list(map(int, list(input())))

result = s[0]
for val in s[1:]:
    result = max(val*result, val + result)

print(result)