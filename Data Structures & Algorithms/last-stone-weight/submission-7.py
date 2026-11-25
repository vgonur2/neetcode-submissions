import heapq
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        bag = []
        for i in stones:
            heapq.heappush(bag,-i)
        while len(bag) > 1:
            x = -1*heapq.heappop(bag)
            y = -1*heapq.heappop(bag)
            if (x < y) or (x > y):
                heapq.heappush(bag, -(abs(y-x)))
        if bag == []:
            return 0
        else:
            return -bag[0]
        
        


