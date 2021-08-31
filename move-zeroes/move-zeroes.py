class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        num = 0
        for i in range(len(nums)-1, -1, -1):
            if nums[i] == 0:
                num += 1
                nums.pop(i)
        nums += [0] * num
        return nums