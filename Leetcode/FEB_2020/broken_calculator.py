def broken_calculator2(x, y):
    n_operations = 0
    while y > x:
        if y & 1 == 0:
            y = y >> 1
        else:
            y += 1  
        n_operations += 1
    return n_operations + x - y

# def broken_calculator_old(x, y):
#     counts = []
    
#     def next_result(x, n_calc):
#         if n_calc > min(counts):
#             return
#         if x == y:
#             counts.append(n_calc)
#             return
#         elif x > y:
#             counts.append(n_calc + x - y)
#             return
#         else:
#             next_result(x-1, n_calc + 1)
#             next_result(x*2, n_calc + 1)

#     if x > y:
#         result = x - y
#     elif x == y:
#         result = 0
#     else:
#         count = 0
#         new_x = x
#         while new_x < y:
#             new_x *= 2
#             count += 1
#         counts.append(count + new_x - y)
#         next_result(x, 0)
#         # print(counts)
#         result = min(counts)
#     # print(result)
#     return(result)



if __name__ == "__main__":
    assert(broken_calculator2(1024, 1) == 1023)
    assert(broken_calculator2(5, 8) == 2)
    assert(broken_calculator2(3, 10) == 3)
    print("All examples passed!")

