def is_ideal_permutation_timeout(a):
    prev_val = a[0]
    global_inversion, local_inversion = 0, 0
    for val in a[1:]:
        if val < prev_val: local_inversion += 1
        prev_val = val

    for i, val in enumerate(a):
        global_inversion += len([inversed_val for inversed_val in a[i+1:] if inversed_val < val])
        if global_inversion > local_inversion:
            return False   

    return global_inversion == local_inversion


if __name__ == "__main__":
    assert(print(is_ideal_permutation([1,0,2])) == True)
    assert(print(is_ideal_permutation([1,2,0])) == False)
    print("All examples passed")