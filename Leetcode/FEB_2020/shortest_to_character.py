import bisect


def shortest_to_char(s, c):
    loc_c = [i for i, char in enumerate(s) if char == c]
    
    def min_dist(i, char):
        if char == c: return 0
        search_index = bisect.bisect_left(loc_c, i)
        if search_index == 0: return loc_c[0] - i
        if search_index >= len(loc_c): return i - loc_c[-1]
        return min(i - loc_c[search_index - 1], loc_c[search_index] - i)
    
    return [min_dist(i, char) for i, char in enumerate(s)]


def shortest_to_char_better(s, c):
    prev, answer = -(len(s) + 1), []
    
    for i, char in enumerate(s):
        if char == c: prev = i
        answer.append(i - prev)
    
    for i in range(len(s) - 1, -1, -1):
        if s[i] == c: prev = i
        answer[i] = min(answer[i], prev - i)

    return answer



if __name__ == "__main__":
    assert(shortest_to_char("loveleetcode", "e") == [3,2,1,0,1,0,0,1,2,2,1,0])
    assert(shortest_to_char("aaab", "b") == [3,2,1,0])
    print("All samples passed")
    assert(shortest_to_char_better("loveleetcode", "e") == [3,2,1,0,1,0,0,1,2,2,1,0])
    assert(shortest_to_char_better("aaab", "b") == [3,2,1,0])
    print("All samples passed2")
