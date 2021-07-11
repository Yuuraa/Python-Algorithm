import bisect # MyMedianFinder
import heapq # MedianFinder

class MyMedianFinder:
    def __init__(self):
        self.data = []
        self.n_data = 0

    def add_num(self, num):
        bisect.insort(self.data, num)
        self.n_data += 1
    
    def find_median(self):
        idx = self.n_data // 2
        if self.n_data % 2 == 0:
            return (self.data[idx] + self.data[idx-1]) / 2
        else:
            return self.data[idx]


class MedianFilter:
    def __init__(self):
        self.small, self.large = [], []

    def add_num(self, num):
        heapq.heappush(self.small, -num)
        heapq.heappush(self.large, -heapq.heappop(self.small))

        if len(self.small) < len(self.large):
            heapq.heappush(self.small, -heapq.heappop(self.large))

    
    def find_median(self):
        if len(self.large) != len(self.small):
            return -self.small[0]
        else:
            return (self.large[0] - self.small[0]) / 2
