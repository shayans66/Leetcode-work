class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
#         dct = {}
#         for n in nums:
#             if n not in dct:
#                 dct[n] = 1
#             else:
#                 dct[n] += 1
#         tot = 1
#         for key,val in dct.items():
#             print(key,val)
#             tot *= key * val
            
#         print(dct)
#         print(tot)
#         for i in range(len(nums)):
#             n = nums[i]
#             nums[i] = tot - n*dct[n] + n*(dct[n]-1)
#         return nums

        res = [1] * len(nums)
        for i in range(1, len(nums)):
            res[i] = res[i-1] * nums[i-1]
        right = 1
        for i in range(len(nums)-1, -1, -1):
            res[i] *= right
            right *= nums[i]
        return res