def is_isomorphic(s, t):
    iso_char, iso_char2 = {}, {}
    for i in range(len(s)):
        c1, c2 = s[i], t[i]
        if c1 in iso_char and iso_char[c1] != c2:
            return False
        if c2 in iso_char and iso_char[c2] != c1:
            return False
        iso_char[c1] = c2
        iso_char[c2] = c1
    return True