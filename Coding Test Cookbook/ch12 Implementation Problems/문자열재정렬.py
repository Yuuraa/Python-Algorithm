import re

s = input()
chars = []
int_val = 0

for c in s:
    if c in '0123456789': int_val += int(c)
    else:
        chars.append(c)

print(''.join(sorted(chars)) + str(int_val))
