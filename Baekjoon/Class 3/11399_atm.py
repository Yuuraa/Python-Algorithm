import sys
from itertools import accumulate


n = int(sys.stdin.readline())
p_list = sorted(map(int, sys.stdin.readline().split()))
print(sum(accumulate(p_list)))
