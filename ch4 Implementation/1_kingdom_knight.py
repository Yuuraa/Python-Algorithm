init_loc = input()
# 좌표를 a1 등에서 -> 0, 0 숫자로 변환
loc_c, loc_r = ord(init_loc[0]) - ord('a'), int(init_loc[1]) - 1
possible_moves = 0

# Knight가 이동할 수 있느 방향들
dr = [-1, 1, -2, -2, 2, 2, -1, 1]
dc = [2, 2, -1, 1, -1, 1, -2, -2]

for i in range(8):
    new_r, new_c = loc_r + dr[i], loc_c + dc[i]
    if new_r >= 0 and new_r < 8 and new_c >= 0 and new_c < 8:
        possible_moves += 1

print(possible_moves)