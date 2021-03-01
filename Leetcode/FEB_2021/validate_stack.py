def validate_stack_sequences(pushed, popped):
    if not pushed: return False
    pop_id = 0
    push_id = pushed.index(popped[0]) + 1
    stack = pushed[:push_id]

    while pop_id < len(popped) and push_id <= len(pushed):
        if not stack or stack[-1] != popped[pop_id]:
            if push_id >= len(pushed): return False
            stack.append(pushed[push_id])
            push_id += 1
        else:
            pop_id += 1
            stack.pop()

    return len(stack) == 0 and push_id >= len(pushed)


if __name__ == "__main__":
    assert(validate_stack_sequences([1, 2, 3, 4, 5], [4, 5, 3, 2, 1]) == True)
    assert(validate_stack_sequences([1, 2, 3, 4, 5], [5, 4, 3, 2, 1]) == True)
    assert(validate_stack_sequences([1, 2, 3, 4, 5], [4, 3, 5, 1, 2]) == False)
    assert(validate_stack_sequences([1, 2, 3, 4, 5], [4, 3, 5, 2, 1]) == True)
    print("All examples passed")