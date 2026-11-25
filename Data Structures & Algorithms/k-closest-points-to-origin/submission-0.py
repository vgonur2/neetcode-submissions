import math
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        distance_list = []
        return_list = []
        for i in points:
            x1 = i[0]
            y1 = i[len(i)-1]
            distance = (math.sqrt((x1 - 0)**2 + (y1 - 0)**2))
            distance_list.append(distance)
        for i in range(k):
            minimum = min(distance_list)
            return_list.append(points[distance_list.index(minimum)])
            points.pop(distance_list.index(minimum))
            distance_list.remove(minimum)

        return return_list
        

                