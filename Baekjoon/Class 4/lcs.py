from collections import defaultdict

s1 = str(input())
s2 = str(input())

subseq_length = [[0 for _ in range(len(s2) + 1)] for _ in range(len(s1) + 1)]

for i in range(len(s1)):
    for j in range(len(s2)):
        if s1[i] == s2[j]:
            subseq_length[i+1][j+1] = subseq_length[i][j] + 1
        else:
            subseq_length[i+1][j+1] = max(subseq_length[i][j+1], subseq_length[i+1][j])

print(subseq_length[-1][-1])

    