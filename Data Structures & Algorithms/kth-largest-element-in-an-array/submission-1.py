import heapq
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        box = []
        x = None
        for i in nums:
            heapq.heappush(box, -i)
        for i in range(k):
            x = -1*heapq.heappop(box)
        return x

        