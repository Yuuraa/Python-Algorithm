def spellchecker(wordlist, queries):
    vowels = 'aeiou'
    results = []

    def spellcheck(query, wordlist):
        for word in wordlist:
            result = ''
            if len(query) != len(word): continue
            
            for c1, c2 in zip(query, word):
                if c1 in vowels and c2 in vowels:
                    result += c2
                elif c1 == c2:
                    result += c2
                else:
                    break
            if result == word:
                return result
        
        return ''

    for query in queries:
        results.append(spellcheck(query, wordlist))
    
    return results