class Solution:
    def maxArea(self, height: List[int]) -> int:
#         if len(height) <= 1:
#             return -1
        
#         maxCur = [0, 0]
#         maxSoFar = 0
        
#         for i in range(1, len(height)):
#             new_area = max(maxCur[1], (i - maxCur[0]) * min(height[maxCur[0]], height[i]), height[i] )
#             if new_area != maxCur[1]:
#                 maxCur[1] = new_area
#                 if maxCur[1] == height[i]:
#                     maxCur[0] = i
            
#             maxSoFar = max(maxSoFar, maxCur[1])
        
#         return maxSoFar

        l, r = 0, len(height)-1
        water = 0
        while(l<=r):
            water = max(water, (r-l) * min(height[l], height[r]))
            if height[l] < height[r]:
                l += 1
            else:
                r -= 1
                
            
            
        return water