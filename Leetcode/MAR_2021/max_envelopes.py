def max_envelopes(envelopes):
    w_outter, h_outter = 0, 0
    ans = 0
    envelopes.sort(key=lambda x: (x[0], x[1]))

    for w, h in envelopes:
        if w > w_outter and h > h_outter:
            ans += 1
            w_outter, h_outter = w, h
    
    return(ans)


print(max_envelopes([[1,1],[1,1],[1,1]]))
print(max_envelopes([[5,4],[6,4],[6,7],[2,3]]))
print(max_envelopes([[2,100],[3,200],[4,300],[5,500],[5,400],[5,250],[6,370],[6,360],[7,380]])) # 5