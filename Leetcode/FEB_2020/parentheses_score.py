def score_of_parentheses(s):
    total_val = 0

    l_count= curr_val = r_count = 0
    c_stack = []
    for c in s:
        if c == "(":
            if r_count > 0:
                total_val += curr_val * (1 << (l_count - 1))
            r_count = curr_val = l_count = 0
            c_stack.append("(")
        if c == ")":
            if r_count == 0:
                l_count = len(c_stack)
                curr_val = 1
            r_count += 1
            c_stack.pop()
    
    total_val += curr_val * (1 << (r_count - 1))
    return total_val


def score_of_parentheses_other(s):
    ans, bal = 0, 0
    for i, c in enumerate(s):
        bal = bal + 1 if c ==  "(" else bal - 1
        if i > 0 and s[i-1:i+1] == "()":
            ans += 1 << bal
    return ans


if __name__ == "__main__":
    assert(score_of_parentheses("(()(()))") == 6)
    assert(score_of_parentheses("()()") == 2)
    assert(score_of_parentheses("()") == 1)
    assert(score_of_parentheses("(())") == 2)
    assert(score_of_parentheses("(())()") == 3)
    print("All examples passed")

