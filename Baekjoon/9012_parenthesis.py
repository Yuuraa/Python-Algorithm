import sys

n = int(input())
strings = []
for _ in range(n):
    strings.append(sys.stdin.readline()[:-1])

def valid_parenthesis(par_str):
    par_stack = []
    for c in par_str:
        if not par_stack:
            if c == ")":
                return "NO"
            par_stack.append(c)
        else:
            if par_stack[-1] == "(" and c == ")":
                par_stack.pop()
            else:
                par_stack.append(c)
    # print(par_stack)
    return "YES" if not par_stack else "NO"


for string in strings:
    print(valid_parenthesis(string))