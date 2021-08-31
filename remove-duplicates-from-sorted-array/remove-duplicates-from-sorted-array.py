class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        # i, j = 0, 0
        # for i in range(0, len(nums)-1):
        #     if(nums[i] < nums[i+1]):
        #         nums[j] = nums[i]
        #         j+=1
        # return j+1
        k= 0

        for i in range(len(nums)-2,-1,-1):
            if nums[i] == nums[i+1]:
                nums.pop(i)
                k+=1
        return len(nums)