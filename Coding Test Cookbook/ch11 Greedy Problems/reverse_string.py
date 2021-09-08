s = list(input())

curr, to = s[0], s[0]
count, total_count = 0, 1
for c in s:
    if c == curr:
        continue
    else:
        if c != to:
            count += 1
        curr = c
        total_count += 1

print(min(count, total_count - count))