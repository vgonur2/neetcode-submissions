class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        new_list = sorted(nums)
        return new_list[len(new_list)-k]