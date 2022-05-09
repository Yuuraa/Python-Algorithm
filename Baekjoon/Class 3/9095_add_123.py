import sys


cnt_buffer = {1: 1, 2: 2, 3: 4}

def get_123_cnt(n):
    if n not in cnt_buffer:
        cnt_buffer[n] = get_123_cnt(n-1) + get_123_cnt(n-2) + get_123_cnt(n-3)
    return cnt_buffer[n]


T = int(sys.stdin.readline())
for _ in range(T):
    print(get_123_cnt(int(sys.stdin.readline())))