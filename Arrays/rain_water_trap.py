class Solution:
    def trap(self, height: List[int]) -> int:
        ans = 0
        n = len(height)
        lmax = 0
        rmax = 0
        side_bars = []
        for i in range(n):
            lmax = max(lmax,height[i])
            side_bars.append([lmax,-1])
            
        for j in range(-1,-1* (n+1),-1):
            rmax = max(rmax,height[j])
            side_bars[j][1] = rmax

        for i in range(n):
            lmax,rmax = side_bars[i]
            ans += min(lmax,rmax) - height[i]
            
        return ans