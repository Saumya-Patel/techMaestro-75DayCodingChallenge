class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        x = nums.count(0)
        for i in range(x):
            
            nums.remove(0)
            nums.append(0)
            
