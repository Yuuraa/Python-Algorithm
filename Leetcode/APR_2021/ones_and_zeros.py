from collections import Counter

def find_max_form(strs, m, n):
    str_counters = list(map(Counter, strs))
    str_counters.sort(key=lambda x: (x['0'], x['1']))
    
    ans = 0
    for binstr in str_counters:
        if binstr["0"] <= m and binstr["1"] <= n:
            m -= binstr["0"]
            n -= binstr["1"]
            ans += 1
    return ans



print(find_max_form(strs = ["10","0001","111001","1","0"], m = 5, n = 3))
print(find_max_form(strs = ["10","0","1"], m = 1, n = 1))
print(find_max_form(["111","1000","1000","1000"], 9, 3)) # 3