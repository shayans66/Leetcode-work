class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # nums = [2,7,11,15], target = 9
        # 1st iter: key: 9-2=7, value= 0
        # 2nd iter: check if 7 is in dict -> it is! -> 
        # return current index of 7 and value of 2 in dict -> return [0,1]

        dct = {}
        for i in range(len(nums)):
            if nums[i] in dct:
                return [i, dct[nums[i]]]
            dct[target - nums[i]] = i
        return -1
        