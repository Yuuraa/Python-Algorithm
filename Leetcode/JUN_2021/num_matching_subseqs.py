from collections import Counter

def is_suqseq(main_str, comp_str):
    stack = list(comp_str)
    main_idx = len(main_str) - 1
    
    while stack:
        if main_idx < 0: return False
        if main_str[main_idx] == stack[-1]:
            stack.pop()
        main_idx -= 1
    return True

def num_matching_subseq(s, words):
    ans = 0
    for word, num_word in Counter(words).items():
        if is_suqseq(s, word):
            ans += num_word
    return ans


if __name__ == "__main__":
    test_cases = [
        ["abcde", ["a","bb","acd","ace"], 3],
        ["dsahjpjauf", ["ahjpjau","ja","ahbwzgqnuk","tnmlanowax"], 2],
    ]

    for s, words, ans in test_cases:
        assert(num_matching_subseq(s, words) == ans)

    print("All test passed!")