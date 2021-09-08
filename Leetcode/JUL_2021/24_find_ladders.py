from collections import defaultdict


def get_adjWords(wordList):
    adjWords = defaultdict(set)
    for w in set(wordList):
        for w2 in set(wordList):
            diff_cnt = 0
            for i in range(len(w)):
                if w[i] != w2[i]:
                    diff_cnt += 1
            if diff_cnt == 1:
                adjWords[w].add(w2)
    return adjWords


def get_dists(wordList, endWord):
    dists = {}
    for w in wordList:
        diff_cnt = 0
        for i in range(len(w)):
            if w[i] != endWord[i]:
                diff_cnt += 1
        dists[w] = diff_cnt
    return dists



def findLadders(beginWord, endWord, wordList):
    if endWord not in wordList: return []
    adjWords = get_adjWords(wordList + [beginWord])
    endDists = get_dists(wordList + [beginWord], endWord)

    



    

