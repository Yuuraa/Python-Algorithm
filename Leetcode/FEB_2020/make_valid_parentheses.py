def rm_make_valid(s):
    par_stack = []
    
    for i, c in enumerate(s):
        if c == "(":
            par_stack.append((c, i))
        elif c == ")":
            if par_stack and par_stack[-1][0] == "(":
                par_stack.pop()
            else:
                par_stack.append((c, i))

    invalid_inidices = [idx for _, idx in par_stack]
    new_s = ''.join([c for i, c in enumerate(s) if i not in invalid_inidices])
    
    return new_s


def rm_make_valid_other(s):
    def clean(s, op, cl):
        balance, ans = 0, ""
        for i in s:
            if i == op:
                balance += 1
                ans += i
            elif i == cl and balance > 0:
                balance -= 1
                ans += i
            elif i not in "()":
                ans += i
        return ans
    return clean(clean(s, "(", ")")[::-1], ")", "(")[::-1]

if __name__ == "__main__":
    assert(rm_make_valid("lee(t(c)o)de)") in ["lee(t(c)o)de", "lee(t(co)de)" , "lee(t(c)ode)"])
    assert(rm_make_valid("a)b(c)d") == "ab(c)d")
    assert(rm_make_valid("))((") == "")
    assert(rm_make_valid("(a(b(c)d)") in ["a(b(c)d)", "(a(bc)d)", "(ab(c)d)"])
    print("All examples passed!")