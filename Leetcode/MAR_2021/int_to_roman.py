def int_to_roman(num):
    ones = ['I', 'X', 'C', 'M']
    fives = ['V', 'L', 'D']

    ans = []
    for i, val in enumerate(str(num)[::-1]):
        val = int(val)
        if int(val) == 4:
            ans.append(fives[i])
            ans.append(ones[i])
        elif int(val) ==  9:
            ans.append(ones[i+1])
            ans.append(ones[i])
        else:
            for _ in range(val%5):
                ans.append(ones[i])
            if val // 5 > 0:
                ans.append(fives[i])
    
    ans_str = ''.join(ans[::-1])
    return(ans_str)


def int_to_roman_other(num):
    def digit(a, b, c, dig):
        return ["", a, 2*a, 3*a, a+b, b, b+a, b+2*a, b+3*a, a+c][dig]
    
    l = ["I", "V", "X", "L", "C", "D", "M", "!", "!"]
    out, i = "", 0

    while num != 0:
        num, last = divmod(num, 10)
        out = digit(l[i], l[i+1], l[i+2], last) + out
        i += 2
    return out



if __name__ == "__main__":
    assert (int_to_roman(9) == "IX")
    assert (int_to_roman(8) == "VIII")
    assert (int_to_roman(1994) == "MCMXCIV")
    print("All examples passed")