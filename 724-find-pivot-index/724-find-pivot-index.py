class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        ls,rs = 0,sum(nums)
        for i,a in enumerate(nums):
            rs -= a
            if ls == rs:
                return i
            ls += a
        return -1