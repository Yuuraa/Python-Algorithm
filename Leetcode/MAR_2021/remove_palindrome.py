def remove_palindromic_subseq(s):
    return 0 if len(s) == 0 else 1 if s == s[::-1] else 2 
