class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
#         l = len(nums)
#         for i in range(l):
#             for j in range(l):
#                 if i != j and nums[i] == nums[j]:
#                     return True
                
#         return False
        
        dct = {}
        for el in nums:
            if el in dct.keys():
                return True
            dct[el] = 1
        return False
        
        