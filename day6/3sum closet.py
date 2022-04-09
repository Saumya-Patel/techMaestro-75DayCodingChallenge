class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        n = len(nums)
        closest = nums[0] + nums[1] + nums[2]
        for i in range(n - 2):
            if i > 0 and nums[i] == nums[i-1]:
                continue 
            l, r = i+1, n-1
            while l < r:
                currSum = nums[i] + nums[l] + nums[r]
                if currSum == target:
                    return target 
                if abs(currSum - target) < abs(closest - target):
                    closest = currSum
                if currSum > target:
                    r -= 1
                else:
                    l += 1
        return closest
