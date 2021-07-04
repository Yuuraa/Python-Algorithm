from collections import defaultdict


def count_vowel_permutation(n):
    formation_rules = { 'a': ['e'], 
                        'e': ['a', 'i'], 
                        'i': ['a', 'e', 'o', 'u'],
                        'o': ['i', 'u'],
                        'u': ['a'] }
    
    vowel_counts = {v: 1 for v in formation_rules.keys()} # n = 1 일 때 초기 단계
    for _ in range(n - 1):
        new_vowel_counts = defaultdict(int)
        for v in vowel_counts:
            for next_v in formation_rules[v]:
                new_vowel_counts[next_v] += vowel_counts[v] % (10**9 + 7)
        vowel_counts = new_vowel_counts

    return sum(vowel_counts.values()) % (10**9 + 7)


if __name__ == "__main__":
    assert (count_vowel_permutation(1) == 5)
    assert (count_vowel_permutation(2) == 10)
    assert (count_vowel_permutation(5) == 68)
    print("All test cases passed!")