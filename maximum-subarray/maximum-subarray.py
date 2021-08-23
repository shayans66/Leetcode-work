class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxCur, maxSoFar = nums[0], nums[0]
        for i in range(1, len(nums)):
            maxCur = max(nums[i], nums[i] + maxCur)
            maxSoFar = max(maxSoFar, maxCur)
        return maxSoFar