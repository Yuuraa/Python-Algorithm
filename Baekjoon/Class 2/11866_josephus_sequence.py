n, k = map(int, input().split())

people = [i+1 for i in range(n)]
seq = []

curr = k - 1
while people:
    seq.append(str(people.pop(curr)))
    if people:
        curr = (curr + k - 1) % len(people)

ans = '<' + ', '.join(seq) + '>'
print(ans)


