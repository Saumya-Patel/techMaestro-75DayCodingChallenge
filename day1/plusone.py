class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        num = ''.join(map(str,digits))
        n = int(num)
        input = [n+1]
        
        lst = list(map(int,str(input[0])))
        
        return lst
