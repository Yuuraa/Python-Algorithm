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


if __name__ == "__main__":
    assert(shortest_to_char("loveleetcode", "e") == [3,2,1,0,1,0,0,1,2,2,1,0])
    assert(shortest_to_char("aaab", "b") == [3,2,1,0])
    print("All samples passed")