# 8 * 8 크기로 잘라낸 후에 진행한다
n, m = map(int, input().split())
boards = []

for _ in range(n):
    boards.append(input())

board_colors = ["B", "W"]

min_repaint_count = m*n + 1
for start_r in range(n - 7):
    for start_c in range(m - 7):
        repaint_count = 0
        for i in range(start_r, start_r + 8):
            check_start = i % 2
            for j in range(start_c, start_c + 8):
                check_curr = (check_start + j) % 2
                if boards[i][j] != board_colors[check_curr]:
                    repaint_count += 1
        # print(min(repaint_count, 64 - repaint_count))
        min_repaint_count = min(min_repaint_count, min(repaint_count, 64 - repaint_count))
print(min_repaint_count)