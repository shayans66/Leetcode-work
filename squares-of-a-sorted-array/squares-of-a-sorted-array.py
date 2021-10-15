class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        nums = [abs(e) for e in nums]
        nums.sort()
        return [e**2 for e in nums]