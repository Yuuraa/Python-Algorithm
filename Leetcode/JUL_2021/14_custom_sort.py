def custom_string(order, s):
    order_dict = {c: i for i, c in enumerate(order)}

    changable = sorted([c for c in s if c in order], key=lambda x: order_dict[x])

    idx = 0
    ordered_chars = []
    for i in range(len(s)):
        if s[i] in order:
            ordered_chars.append(changable[idx])
            idx += 1
        else:
            ordered_chars.append(s[i])

    return "".join(ordered_chars)
