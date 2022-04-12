class Solution:
    def findPairs(self, nums: List[int], k: int) -> int:
        nums = sorted(nums) 
        numdict = dict()
        res = set()
        
        for n in nums :
            if n in numdict :
                res.add((n,numdict[n]))
            numdict[k+n]=n
                
        return len(res)
