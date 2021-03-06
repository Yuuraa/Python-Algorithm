from collections import Counter

result = []
n = int(input())
cards = list(map(int, input().split()))
num_cards = Counter(cards)

m = int(input())
check_vals = list(map(int, input().split()))
for check_val in check_vals:
    if check_val in num_cards:
        result.append(str(num_cards[check_val]))
    else:
        result.append('0')

print(' '.join(result))
