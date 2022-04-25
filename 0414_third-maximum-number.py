import heapq


class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        heap = []
        for num in nums:
            if num in heap:
                continue
            heapq.heappush(heap, num)
            if len(heap) > 3:
                heapq.heappop(heap)
        if len(heap) == 3:
            return heapq.heappop(heap)
        else:
            return max(heap)
