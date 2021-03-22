# 문제를 해결하지 못한 spell checker.. 내 생각에는 diff_count로 가장 가까운 단어를
# 추천해 주는 것이 맞는 것 같은데, 문제의 요구사항과는 달랐다 
def spellcheck_old_helper(wordlist, query):
    vowels = "aeiouAEIOU"
    
    possible_results = []
    for word in wordlist:
        if len(word) != len(query): continue
        result, diff_count = '', 0

        for c1, c2 in zip(query, word):
            if c1.lower() == c2.lower():
                result += c2
            elif c1 in vowels and c2 in vowels:
                result += c2
                diff_count += 1
            else:
                break
        if result == word:
            possible_results.append((result, diff_count))

    return sorted(possible_results, key=lambda x: x[1])[0][0] if possible_results else ''


# spellchecker solution
def spellchecker(wordlist, queries):
    def devowel(word):
        return ''.join('*' if c in 'aeiou' else c for c in word)

    words_perfect = set(wordlist)
    words_cap = {}
    words_vow = {}

    for word in wordlist:
        wordlow = word.lower()
        words_cap.setdefault(wordlow, word)
        words_vow.setdefault(devowel(wordlow), word)

    
    def solve(query):
        if query in words_perfect:
            return query
        
        queryL = query.lower()
        if queryL in words_cap:
            return words_cap[queryL]

        queryLV = devowel(queryL)
        if queryLV in words_vow:
            return words_vow[queryLV]
        return ""
    
    return map(solve, queries)