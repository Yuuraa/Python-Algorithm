from collections import defaultdict
# def get_adj_words(beginWord, wordList):


# DFS, 재귀 함수로 짰고 시간 초과 난 함수
"""
def find_ladders(beginWord, endWord, wordList):
    if endWord not in wordList: return []
    # adj_words = get_adj_words(beginWord, wordList)
    adj_words = defaultdict(set)
    for w in wordList + [beginWord]:
        for w2 in wordList + [beginWord]:
            assert(len(w) == len(w2))
            diff_cnt = 0
            for i in range(len(w)):
                if w[i] != w2[i]: diff_cnt += 1
            if diff_cnt == 1: adj_words[w].add(w2)

    minPaths = []
    def find_ladder(currPath, endWord):
        currWord = currPath[-1]
        if minPaths and len(minPaths[0]) < len(currPath): return

        # 마지막에 다다랐을 경우를 확인함
        if currWord == endWord:
            if not minPaths or len(minPaths[0]) == len(currPath):
                minPaths.append(currPath)
            else:
                if len(minPaths[0]) > len(currPath):
                    minPaths.clear()
                    minPaths.append(currPath)
            return
        
        for w in adj_words[currWord]:
            if w not in currPath:
                find_ladder(currPath + [w], endWord)
    
    find_ladder([beginWord], endWord)

    return minPaths
"""

# def get_adjacents(word_list):
#     adj_words = defaultdict(set)
#     for w in word_list:
#         for w2 in word_list:
#             diff_cnt = 0
#             assert len(w) == len(w2)
#             for i in range(len(w)):
#                 if w[i] != w2[i]:
#                     diff_cnt += 1
#             if diff_cnt == 1: adj_words[w].add(w2)
#     return adj_words


# def get_next_paths(path, adj_words):
#     last_word = path[-1]
#     next_paths = []
#     for w in adj_words[last_word]:
#         if w not in path:
#             next_paths.append(path + [w])
#     return next_paths


# def find_ladders(beginWord, endWord, wordList):
#     adjWords = get_adjacents(wordList + [beginWord])
#     print(adjWords)
#     paths = [[beginWord]]
#     if endWord not in wordList: return []
#     minpath = []

#     while paths and not minpath:
#         new_paths = []
#         for p in paths:
#             next_paths = get_next_paths(p, adjWords)
#             print(next_paths)
#             for np in next_paths:
#                 if np[-1] == endWord: 
#                     minpath.append(np)
#             new_paths.extend(next_paths)
#         paths = new_paths
    
#     return minpath




# print(find_ladders(beginWord = "hit", endWord = "cog", wordList = ["hot","dot","dog","lot","log","cog"]))
print(find_ladders(beginWord = "a", endWord = "c", wordList = ["a", "b", "c"]))