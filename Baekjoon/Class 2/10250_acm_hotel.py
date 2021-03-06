t = int(input())

import sys
ans = []
for _ in range(t):
    h, w, customer_num = map(int, sys.stdin.readline().split())
    room_w = customer_num // h + 1
    room_h = customer_num % h
    if room_h == 0:
        room_h = h
        room_w -= 1
    ans.append((room_h, room_w))

for room_h, room_w in ans:
    print(f'{room_h}{room_w:02d}')