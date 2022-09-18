class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not len(nums): return 0
        nums.sort()
        cur = 1
        i = 0
        mx = 1
        while i < len(nums):
            if nums[i] == nums[i-1]+1:
                cur +=1
                i += 1
            elif nums[i] == nums[i-1]:
                i += 1
            else:
                cur = 1
                i += 1
            mx = max(mx, cur)
        return mx