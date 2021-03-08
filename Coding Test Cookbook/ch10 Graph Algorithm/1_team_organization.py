n, m = map(int, input().split())

# 맨 처음에는 1인팀
teams = [i for i in range(n + 1)]

def find_team(teams, a):
    if teams[a] != a:
        teams[a] = find_team(teams, teams[a])
    return teams[a]

def union_find(teams, a, b):
    a = find_team(teams, a)
    b = find_team(teams, b)

    if a < b:
        teams[b] = a
    else:
        teams[a] = b



# 팀 합치기 연산을 받음
results = []
for _ in range(m):
    oper, a, b = map(int, input().split())
    if oper == 1:
        if find_team(teams, a) == find_team(teams, b):
            results.append("YES")
        else:
            results.append("NO")
    else:
        union_find(teams, a, b)

print(results, end="\n")


# 실행 결과
# 7 8
# 0 1 3
# 1 1 7
# 0 7 6
# 1 7 1
# 0 3 7
# 0 4 2
# 0 1 1 
# 1 1 1 
# ['NO', 'NO', 'YES']