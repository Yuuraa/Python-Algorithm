def distribute_candies(candy_type):
    return min(len(set(candy_type)), len(candy_type)//2)