n = int(input())

tiles =  [0 for i in range(n + 1)]
tiles[1], tiles[2] = 1, 3
for i in range(3, n + 1):
    tiles[i] = (tiles[i-1] + 2*tiles[i-2]) % 796796

print(tiles[n])
