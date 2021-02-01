n = int(input())
movements = list(input().split())

dr = [1, 0, -1, 0]
dc = [0, 1, 0, -1]
movement_dic = {'R': 1, 'L': 3, 'U': 2, 'D': 0}
loc_r, loc_c = 1, 1

for move in movements:
    move_id = movement_dic[move]
    new_r, new_c = loc_r + dr[move_id], loc_c + dc[move_id]
    # 공간을 넘어가는 경우 고려하지 않음
    if new_r < 1 or new_r > n or new_c < 1 or new_c > n:
        continue
    # 이동함
    else:
        loc_r, loc_c = new_r, new_c

print(loc_r, loc_c)