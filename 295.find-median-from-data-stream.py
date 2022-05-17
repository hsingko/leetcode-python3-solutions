#
# @lc app=leetcode id=295 lang=python3
#
# [295] Find Median from Data Stream
#

# @lc code=start

import heapq


class MaxHeap:
    def __init__(self) -> None:
        self.heap = []
    def push(self, val):
        heapq.heappush(self.heap, -val)
    def pop(self):
        return -heapq.heappop(self.heap)
    def peek(self):
        return self.heap[0]*-1
    def size(self):
        return len(self.heap)
    def not_empty(self):
        return bool(self.heap)

class MinHeap:
    def __init__(self) -> None:
        self.heap = []
    def push(self, val):
        heapq.heappush(self.heap, val)
    def pop(self):
        return heapq.heappop(self.heap)
    def peek(self):
        return self.heap[0]
    def size(self):
        return len(self.heap)
    def not_empty(self):
        return bool(self.heap)
        
class MedianFinder:

    def __init__(self):
        self.left = MaxHeap()
        self.right = MinHeap()

    def addNum(self, num: int) -> None:
        left = self.left
        right = self.right

        left.push(num)
        if left.not_empty() and right.not_empty() and (left.peek() > right.peek()):
            right.push(left.pop())
        if left.size() > right.size()+1:
            right.push(left.pop())
        if right.size() > left.size() + 1:
            left.push(right.pop())

    def findMedian(self) -> float:
        left = self.left
        right = self.right
        if left.size() > right.size():
            return left.peek()
        if right.size() > left.size():
            return right.peek()
        return (left.peek()+right.peek())/2


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()
# @lc code=end

