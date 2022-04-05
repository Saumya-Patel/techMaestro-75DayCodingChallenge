class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        a =[]
        for i in range(len(nums)):
            x = nums[i]**2
            a.append(x)
        return sorted(a)
