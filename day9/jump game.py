class Solution:
    def canJump(self, nums: List[int]) -> bool:
        jump = 0 
        for i in nums[:-1]:
            jump = max(jump, i) 
            if jump <= 0: 
                return False
            jump -= 1 
        return True 
