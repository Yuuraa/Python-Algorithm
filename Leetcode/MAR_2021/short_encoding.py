def min_length_encoding(words):
    words = sorted([s[::-1] for s in set(words)])
    encoded_wordset = set(words)

    def included_word(w1, w2):
        min_length = min(len(w1), len(w2))
        for c1, c2 in zip(w1[:min_length], w2[:min_length]):
            if c1 != c2:
                return False
        else:
            return True

    for i in range(len(words) - 1):
        if included_word(words[i], words[i+1]):
            if len(words[i]) > len(words[i + 1]):
                encoded_wordset -= set([words[i+1]])
            else: encoded_wordset -= set([words[i]])

    ans = "#".join(list(encoded_wordset)) + "#"
    return len(ans)


class TrieNode:
    def __init__(self):
        self.children = {}

class Tire:
    def __init__(self):
        self.root = TrieNode()
        self.ends = []

    def insert(self, word):
        root = self.root
        for symbol in word:
            root = root.children.setdefault(symbol, TrieNode())
        self.ends.append((root, len(word) + 1))


def trienode_encoding(words):
    trie, ans = Trie(), 0

    for word in set(words):
        trie.insert(word[::-1])

    return sum(depth for node, depth in trie.ends if len(node.childern)==0)
    