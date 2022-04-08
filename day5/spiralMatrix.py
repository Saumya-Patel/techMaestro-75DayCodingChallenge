class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        x=0
        y=0
        op =[]
        m = len(matrix)
        n = len(matrix[0])
        left=0
        right =n-1
        up =1
        down =m-1
        
        op.append(matrix[y][x])
        while left<= right and up-1 <= down:
            while x < right:
                x += 1
                op.append(matrix[y][x])
            right -= 1
            
            while y < down:
                y += 1
                op.append(matrix[y][x])
            down -= 1
            
            while x > left:
                x -= 1
                op.append(matrix[y][x])
            left += 1
            
            while y > up:
                y -= 1
                op.append(matrix[y][x])
            up += 1
        
        return op[:n*m]
        
        
        
    
