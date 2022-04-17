class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
    
        stack, ans = [-1], []
        for i, n in enumerate(heights):
            while len(stack) > 1 and heights[stack[-1]] >= n:
                ans += heights[stack.pop()] * (i - stack[-1] - 1),
            stack += i,

        while len(stack) > 1:
            ans += heights[stack.pop()] * (len(heights) - stack[-1] - 1),

        return max(ans)
