def push_dominoes(dominoes):
    lr, ll = -1, -1
    ans = ''
    for i, dominoe in enumerate(dominoes):
        if dominoe == 'R':
            if lr <= ll:
                ans += '.' * (i-ll-1)
            else:
                ans += 'R' * (i-lr-1)
            lr = i
            ans += 'R'
        elif dominoe == 'L':
            if ll >= lr:
                ans += 'L' * (i -ll - 1)
            else:
                btw = i - lr - 1
                middle_block = '.' if btw % 2 != 0 else ''
                ans += 'R'*(btw//2) + middle_block + 'L'*(btw//2)
            ll = i
            ans += 'L'
        print(i, ans)
    
    if ans and ans[-1] == 'R':
        ans += "R" * (len(dominoes) - len(ans))
    else:
        ans += "." * (len(dominoes) - len(ans))

    return ans


print(push_dominoes("RR.L"))
print(push_dominoes(".L.R...LR..L.."))