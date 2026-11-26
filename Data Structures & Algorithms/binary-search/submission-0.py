class Solution:
    def search(self, nums: List[int], target: int) -> int:
        new_list = nums
        mid = len(nums)//2
        if new_list == []:
            return -1
        while len(new_list) > 2:
            if new_list[mid] == target:
                return nums.index(target)
            elif new_list[mid] < target:
                new_list = new_list[mid:]
                mid = len(new_list)//2
            else:
                new_list = new_list[:mid+1]
                mid = len(new_list)//2
        if (len(new_list) == 1) and (new_list[0] == target):
            return nums.index(target)
        elif (len(new_list) == 2) and ((new_list[0] == target) or (new_list[1] == target)):
            return nums.index(target)
        else:
            return -1



        