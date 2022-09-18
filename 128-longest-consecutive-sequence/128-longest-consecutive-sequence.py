class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums: return 0
        nums.sort()
        
        i,mx,cur = 1,1,1
        
        while i <len(nums):
            if nums[i] == nums[i-1]+1:
                i += 1
                cur += 1
            elif nums[i] == nums[i-1]:
                i+=1
            else:
                i+=1
                cur = 1
            mx = max(mx, cur)
        return mx
                