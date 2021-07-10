def cnt_combinable_case(s, i):
    combi_count = 0
    if s[i] in '1*':
        if s[i+1] == '*':
            combi_count += 9
        else: combi_count += 1
    if s[i] in '2*':
        if s[i+1] == '*':
            combi_count += 6
        elif s[i+1] in '123456': combi_count += 1
    return combi_count

def num_partial_decodings(s):
    dp = [1 for _ in range(len(s)+1)]
    for i in range(len(s) - 1, -1, -1):
        dp[i] = dp[i+1]
        if s[i] == '*': dp[i] += 8 * dp[i+1]
        if i < len(s) - 1: 
            dp[i] += cnt_combinable_case(s, i) * dp[i+2]
        dp[i] %= (10**9 + 7)

    return dp[0]
        

def num_decodings(s):
    substrs = []
    
    curr_str = ""
    mult_factor = 1
    for i, c in enumerate(s):
        if c == '0':
            if not curr_str or curr_str[-1] not in '12*': return 0
            if curr_str[-1] == '*': mult_factor *= 2
            curr_str = curr_str[:-1]
            substrs.append(curr_str)
            curr_str = ""
        else:
            curr_str += c
    substrs.append(curr_str)

    ans = mult_factor
    print(mult_factor)
    for substr in substrs:
        ans *= num_partial_decodings(substr)
        ans %= (10**9 + 7)

    return ans


# print(num_decodings("11106"))
# print(num_decodings("*"))
# print(num_decodings("2*"))
print(num_decodings("*1*1*0")) # 404
