class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        new_sort = sorted(stones)
        global_list = []
        while len(new_sort) > 1:
            x = len(new_sort)-2
            y = len(new_sort)-1
            if new_sort[x] == new_sort[y]:
                global_list = new_sort[:x]
                global_list = sorted(global_list)
                new_sort = global_list
            elif new_sort[x] < new_sort[y]:
                global_list = new_sort[:x]
                global_list.append(abs(new_sort[x] - new_sort[y]))
                global_list = sorted(global_list)
                new_sort = global_list
        print(new_sort)
        if new_sort == []:
            return 0
        for i in new_sort:
            return i


