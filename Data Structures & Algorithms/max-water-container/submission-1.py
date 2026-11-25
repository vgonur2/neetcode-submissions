class Solution:
    def maxArea(self, heights: List[int]) -> int:
        high = 0
        local_highest = 0
        distance = None
        i = 0
        j = len(heights)-1
        while distance != 0:
            distance = j - i
            minimum = min(heights[j], heights[i])
            local_highest = minimum * distance
            if local_highest > high:
                high = local_highest
            if minimum == heights[j]:
                j -=1
            else:
                i += 1
        return high
