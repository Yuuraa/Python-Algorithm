n_items, weight_cap = list(map(int, input().split()))

weights = []
values = []
for _ in range(n_items):
    w, v = list(map(int, input().split()))
    weights.append(w)
    values.append(v)


knapsack_array = [[0 for _ in range(weight_cap + 1)] for _ in range(n_items)]
knapsack_array[0] = [0 if c < weights[0] else values[0] for c in range(weight_cap + 1)]

for i in range(1, n_items):
    w, v = weights[i], values[i]
    for c in range(1, weight_cap + 1):
        if w <= c:
            knapsack_array[i][c] = max(knapsack_array[i-1][c], knapsack_array[i-1][c - w] + v)
        else:
            knapsack_array[i][c] = knapsack_array[i-1][c]

print(knapsack_array[-1][-1])