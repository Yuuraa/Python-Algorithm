n, m = map(int, input().split())
tteok_lengths = list(map(int, input().split()))

def get_cut_length(tteok_lengths, m):
    min_cut, max_cut = 0, max(tteok_lengths)
    while min_cut <= max_cut:
        mid_cut = (min_cut + max_cut) // 2
        customer_amount = sum([max(0, tteok_len - mid_cut) for tteok_len in tteok_lengths])
        if customer_amount == m:
            return mid_cut
        elif customer_amount < m:
            max_cut = mid_cut - 1
        else:
            min_cut = mid_cut + 1
    if customer_amount < m:
        return mid_cut - 1
    return mid_cut

print(get_cut_length(tteok_lengths, m))