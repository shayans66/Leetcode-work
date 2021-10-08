class Solution:
    def maxArea(self, height: List[int]) -> int:
        l,r = 0,len(height)-1
        mx,cur = 0,0
        
        while l < r:
            cur = (r-l) * min(height[l], height[r])
            mx = max(mx, cur)
            
            if height[l] > height[r]:
                r -= 1
            else:
                l+=1
        return mx