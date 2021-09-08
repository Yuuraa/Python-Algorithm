def mukbang(food_times, k):
    n = len(food_times)
    
    curr = 0
    food_list = [[i+1, food_time] for i, food_time in enumerate(food_times)]
    food_list.sort(key=lambda x: x[1])

    for i, (idx, food_time) in enumerate(food_list):
        if k - food_time * n < 0:
            food_list.sort(key = lambda x : x[0])
            for _ in range(k):
                if food_list[curr] == 0:
                    
            break
        else:
            k -= food_time * n


            n -= 1

    return answer
        


print(mukbang([3, 1, 2], 5))