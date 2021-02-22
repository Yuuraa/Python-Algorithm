def find_longest_word(s, d):
    d.sort(key=lambda x:(-len(x), x))

    for d_str in d:
        i, j = 0, 0
        while i < len(d_str) and j < len(s):
            if d_str[i] == s[j]:
                i += 1
            j += 1
        if i >= len(d_str):
            return d_str

    return ""

if __name__ == "__main__":
    assert(find_longest_word(s = "abpcplea", d = ["a","b","c"]))
    assert(find_longest_word(s = "abpcplea", d = ["ale","apple","monkey","plea"]))
    assert(find_longest_word("bab", ["ba","ab","a","b"]))

    print("All examples passed")