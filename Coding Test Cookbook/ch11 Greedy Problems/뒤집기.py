from collections import defaultdict

s = input()
cnt = {'0': 0, '1': 0}
prev = s[0]
cnt[prev] += 1

for c in s:
    if c != prev: 
        cnt[c] += 1
        prev = c

print(min(cnt['0'], cnt['1']))