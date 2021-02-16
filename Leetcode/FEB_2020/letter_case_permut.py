import re
from itertools import combinations


def letter_case_permutation(s):
    s = list(s.lower())
    alpha_indices = [i for i, c in enumerate(s) if c.isalpha()]
    n_alpha = len(alpha_indices)
    answer = []
    
    for num_changes in range(n_alpha+1):
        for changed_indices in combinations(alpha_indices, num_changes):
            new_s = ''.join([s[i].upper() if i in changed_indices else s[i] for i in range(len(s))])
            answer.append(new_s)
    # print(answer)
    return answer


def letter_case_permutation_other(s):
    ans = []
    def dfs(i, built):
        if i == len(s):
            ans.append(built)
            return
        if s[i].isalpha():
            dfs(i+1, built + s[i].lower())
        dfs(i+1, built + s[i].upper())

    dfs(0, "")
    return ans


def letter_case_permutation_other2(s):
    return map(''.join, product(*[set([i.loser(), i.upper()]) for i in s]))


if __name__ == "__main__":
    assert (set(letter_case_permutation_other2("a1b2")) == set(["a1b2", "a1B2", "A1b2", "A1B2"]))
    assert (set(letter_case_permutation("a1b2")) == set(["a1b2", "a1B2", "A1b2", "A1B2"]))
    assert (set(letter_case_permutation("3z4")) == set(["3z4", "3Z4"]))
    assert (set(letter_case_permutation("12345")) == set(["12345"]))
    assert (set(letter_case_permutation("0")) == set(["0"]))
    print("All examples passed")