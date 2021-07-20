import random

class Solution:
    def __init__(self, nums):
        self.nums = nums.copy()
        self.orig = nums

    def reset(self):
        return self.orig
    
    def shuffle(self):
        random.shuffle(self.nums)
        return self.nums