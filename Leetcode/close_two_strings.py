from collections import Counter

def closeStrings(word1, word2):
    if len(word1) != len(word2) or set(word1) != set(word2):
        return False
    counter1, counter2 = Counter(word1), Counter(word2)
    val1 = sorted([val for val in counter1.values()])
    val2 = sorted([val for val in counter2.values()])

    return val1 == val2


if __name__ == "__main__":
    assert(closeStrings("abc", "bca") == True)
    assert(closeStrings("cabbba", "aabbss") == False)
    assert(closeStrings("abbzccca", "babzzczc") == True)
    print("All examples passed!")