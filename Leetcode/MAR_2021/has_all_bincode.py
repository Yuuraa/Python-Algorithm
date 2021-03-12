def has_all_codes(s, k):
    bin_set = set()
    for i in range(len(s) - k+1):
        bin_set.add(s[i:i+k])
        if len(bin_set) == 2**k: return True # 미리 끝내기 위함.
    return len(bin_set) == 2**k


def has_all_codes_other(s, k):
    need = 1<<k
    got = [False]*need
    all_one = need - 1
    hash_val = 0

    for i in range(len(s)):
        hash_val = ((hash_val << 1) & all_one) | (int(s[i]))
        if i >= k - 1 and got[hash_val] is False:
            got[hash_val] = True
            need -= 1
            if need == 0:
                return True
        return False


if __name__ == "__main__":
    assert(has_all_codes("00110110", k = 2) == True)
    assert(has_all_codes(s = "00110", k = 2) == True)
    assert(has_all_codes( s = "0110", k = 1) == True)
    assert(has_all_codes(s = "0110", k = 2) == False)
    assert(has_all_codes(s = "0000000001011100", k = 4) == False)