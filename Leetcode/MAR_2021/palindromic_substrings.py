def count_substrings(s):
    def is_palindrome(substr):
        left, right = 0, len(substr) - 1
        while left < right:
            if substr[left] != substr[right]:
                return False
            left += 1
            right -= 1
        return True
    
    ans = 0
    for i in range(1, len(s) + 1):
        for j in range(len(s) - i + 1):
            if is_palindrome(s[j:j+i]):
                ans += 1
    print(ans)
    return ans

count_substrings("aaa")
count_substrings("abc")