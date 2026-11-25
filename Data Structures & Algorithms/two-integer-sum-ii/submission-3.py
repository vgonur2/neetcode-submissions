class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        i = 0
        j = len(numbers) - 1
        return_list = []
        for k in numbers:
            if numbers[i] == numbers[j]:
                if numbers[i] + numbers[j] == target:
                    return_list.append(i+1)
                    return_list.append(j+1)
                    return return_list
            if numbers[i] + numbers[j] == target:
                return_list.append(i+1)
                return_list.append(j+1)
                return return_list
            elif numbers[i] + numbers[j] < target:
                i +=1 
            else:
                j -=1
                



        