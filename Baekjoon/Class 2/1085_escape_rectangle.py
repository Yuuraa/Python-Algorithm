x, y, w, h = map(int, input().split())
dists = [x, w - x, y, h - y]
print(min(dists))