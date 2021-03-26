from collections import Counter


def word_subsets_timelimit(a, b):
    def is_subset_word(a, word):
        count_a, count_w = Counter(a), Counter(word)
        for c in count_w:
            if c in count_a and count_a[c] >= count_w[c]:
                continue
            else: return False
        return True    


    def check_subset(a, word_list):
        for word in word_list:
            if not is_subset_word(a, word):
                return False
        return True

    ans = []
    for word_a in a:
        if check_subset(word_a, b):
            ans.append(word_a)
    print(ans)
    return ans


from collections import Counter
def word_subsets(a, b):
    b_total_count = {}
    universal_words = []
    
    # b에 있는 모든 단어들에서 등장하는 전체 문자들에 대해 각각 등장 횟수의 최댓값을 구하고, 이를 b_total_count 딕셔너리에 담는다
    for word in b:
        b_word_count = Counter(word)
        for b_char in b_word_count:
            if b_char in b_total_count:
                b_total_count[b_char] = max(b_total_count[b_char], b_word_count[b_char])
            else:
                b_total_count[b_char] = b_word_count[b_char]

    
    for word in a:
        a_word_count = Counter(word)
        is_universal = True
        for b_char in b_total_count:
            if b_char not in a_word_count or a_word_count[b_char] < b_total_count[b_char]:
                is_universal = False
                break
        if is_universal:
            universal_words.append(word)

    print(universal_words)
    return universal_words


    

word_subsets( a = ["amazon","apple","facebook","google","leetcode"], b = ["lo","eo"])
word_subsets(a = ["amazon","apple","facebook","google","leetcode"], b = ["lo","eo"])
word_subsets(a = ["amazon","apple","facebook","google","leetcode"], b = ["ec","oc","ceo"])