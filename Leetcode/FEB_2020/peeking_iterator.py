# Below is the interface for Iterator, which is already defined for you.
#
# class Iterator:
#     def __init__(self, nums):
#         """
#         Initializes an iterator object to the beginning of a list.
#         :type nums: List[int]
#         """
#
#     def hasNext(self):
#         """
#         Returns true if the iteration has more elements.
#         :rtype: bool
#         """
#
#     def next(self):
#         """
#         Returns the next element in the iteration.
#         :rtype: int
#         """

class PeekingIterator:
    def __init__(self, iterator):
        """
        Initialize your data structure here.
        :type iterator: Iterator
        """
        self.iterator = iterator
        self.peeking = False
        self.curr_val = None
        

    def peek(self):
        """
        Returns the next element in the iteration without advancing the iterator.
        :rtype: int
        """
        if self.peeking: return self.curr_val
        else:
            self.curr_val = self.iterator.next()
            self.peeking = True
        return self.curr_val
        

    def next(self):
        """
        :rtype: int
        """
        if self.peeking:
            self.peeking = False
            return self.curr_val
        else:
            return self.iterator.next()

        

    def hasNext(self):
        """
        :rtype: bool
        """
        return self.peeking or self.iterator.hasNext()
        

# Your PeekingIterator object will be instantiated and called as such:
# iter = PeekingIterator(Iterator(nums))
# while iter.hasNext():
#     val = iter.peek()   # Get the next element but not advance the iterator.
#     iter.next()         # Should return the same value as [val].