import sys

n = int(input())
possible_rep = True

from collections import defaultdict

on_numbers = defaultdict(list)
on_numbers[0] = [0, 2, 3, 4, 5, 6, 7, 8, 9]
on_numbers[1] = [0, 2, 3, 5, 6, 7, 8, 9]
on_numbers[2] = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
on_numbers[3] = [0, 4, 5, 6, 8, 9]
on_numbers[4] = []
on_numbers[5] = [0, 1, 2, 3, 4, 7, 8, 9]
on_numbers[6] = [0, 2, 3, 4, 5, 6, 8, 9]
on_numbers[7] = [2, 3, 4, 5, 6, 8, 9]
on_numbers[8] = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
on_numbers[9] = [0, 2, 6, 8]
on_numbers[10] = []
on_numbers[11] = [0, 1, 3, 4, 5, 6, 7, 8, 9]
on_numbers[12] = [0, 2, 3, 5, 6, 8, 9]
on_numbers[13] = [0, 2, 3, 5, 6, 8, 9]
on_numbers[14] = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

ans_set = [set([0, 1, 2, 3, 4, 5, 6, 7, 8, 9]) for i in range(n)]
for j in range(5):
    in_line = sys.stdin.readline()
    idx = j
    for i in range(n):
        vals = in_line[4*i:4*i+3]
        for k, lightbulb in enumerate(vals):
            if lightbulb == "#":
                ans_set[i] &= set(on_numbers[k+3*j])
                if not ans_set[i]:
                    possible_rep = False
                    break

if not possible_rep:
    print(-1)
else:
    rep_nums, val = [0], 1
    for i in range(n):
        if len(ans_set[n-1-i]) == 0:
            possible_rep = False
            break
        else:
            curr_rep = []
            for rep in rep_nums:
                for num in ans_set[n-1-i]:
                    curr_rep.append(rep + num*val)
        rep_nums = curr_rep
        val *= 10
    rep_nums = list(set(rep_nums))
    print(rep_nums)
    print(sum(rep_nums)/len(rep_nums))