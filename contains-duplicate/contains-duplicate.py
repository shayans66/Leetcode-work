class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:

#         dct = {}
#         for el in nums:
#             if el in dct.keys():
#                 return True
#             dct[el] = 1
#         return False
        
        
        nums.sort()
        for i in range(0, len(nums)-1):
            if nums[i] == nums[i+1]:
                return True
        return False