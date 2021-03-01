from collections import Counter


def findLHS(nums):
    num_count = Counter(nums)
    answer = 0

    for n in num_count:
        if n + 1 in num_count:
            answer = max(answer, num_count[n] + num_count[n + 1])



def findLHS_other(nums):
    C = Counter(nums)
    return max((C[n] + C[n+1])*(C[n+1] != 0) for n in C)