class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
#         arr = list(range(1, len(nums) + 1))
#         hm = {}
#         for n in arr:
#             hm[n] = 0
#         print(hm)
#         for n in nums:
#             if n in hm.keys():
#                 del hm[n]
            
            
#         return hm.keys()

#         arr = list(range(1, len(nums) + 1)) # total range
#         uniqNums = []
#         [uniqNums.append(x) for x in nums if x not in uniqNums] # comp of this
#         print(uniqNums)
#         print(arr)
        
#         return [x for x in arr if x not in uniqNums]

        for i in range(len(nums)):
            idx = abs(nums[i]) - 1
            nums[idx] = -abs(nums[idx])
            
        print(nums)
        return [i+1 for i in range(len(nums)) if nums[i] > 0]