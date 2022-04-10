class Solution:
    def jump(self, nums: List[int]) -> int:
       dps = [inf for _ in range(len(nums))]
       dps[0] = 0
        
       for i in range(len(nums)):
        n = nums[i]
        for j in range(1, n+1):
            if i + j < len(nums):
                dps[i+j] = min(dps[i+j], dps[i]+1)
        
       return dps[-1]
 
