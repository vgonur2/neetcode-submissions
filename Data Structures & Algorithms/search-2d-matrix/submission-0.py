class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        x1 = 0
        x2 = len(matrix)-1
        y1 = 0
        y2 = len(matrix[0])-1
        start = matrix[x1][y1]
        start_index = ((x1*(len(matrix[0])))+y1)
        end = matrix[x2][y2]
        end_index = ((x2*(len(matrix[0])))+y2)
        
        while start_index + (end_index - start_index)//2 != start_index:
            if matrix[(start_index+((end_index - start_index)//2))//len(matrix[0])][(start_index+((end_index - start_index)//2))%len(matrix[0])] == target:
                return True
            elif matrix[(start_index+((end_index - start_index)//2))//len(matrix[0])][(start_index+((end_index - start_index)//2))%len(matrix[0])] < target:
                x1 = (start_index+((end_index - start_index)//2))//len(matrix[0])
                y1 = (start_index+((end_index - start_index)//2))%len(matrix[0])
                start = matrix[x1][y1]
                start_index = ((x1*(len(matrix[0])))+y1)
                
            else:
                x2 = (start_index+((end_index - start_index)//2))//len(matrix[0])
                y2 = (start_index+((end_index - start_index)//2))%len(matrix[0])
                end = matrix[x2][y2]
                end_index = ((x2*(len(matrix[0])))+y2)
                
        
        if start == target:
            return True
        elif end == target:
            return True
        else:
            return False
        
