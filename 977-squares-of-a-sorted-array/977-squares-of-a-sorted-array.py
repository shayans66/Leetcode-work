class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        l,r = 0,len(nums)-1
        res = [0] * len(nums)
        # for i in range(len(nums)-1,-1,-1):
        i = len(nums)-1
        while l<=r:
            if nums[l]**2 > nums[r]**2:
                res[i] = nums[l]**2
                l += 1
            else:
                res[i] = nums[r]**2
                r -= 1
            i -= 1
            # print(res)
        return res
    
    """
    1 3
    x x x
    1 3
    1 2
    1 1
    """