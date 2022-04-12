class Solution:
    def maxArea(self, h: int, w: int, horizontalCuts: List[int], verticalCuts: List[int]) -> int:
        horizontalCuts = [0] + horizontalCuts + [h]
        verticalCuts = [0] + verticalCuts + [w]
        
        horizontalCuts.sort()
        verticalCuts.sort()
        hmax = -1
        vmax=-1
        
        for i in range(1,len(horizontalCuts)):
            hmax = max(hmax,horizontalCuts[i]-horizontalCuts[i-1])
        for i in range(1,len(verticalCuts)):
            vmax = max(vmax,verticalCuts[i]-verticalCuts[i-1])
        return (hmax * vmax)%((10**9)+7)
        
