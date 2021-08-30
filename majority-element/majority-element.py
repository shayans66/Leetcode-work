class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        mintimes = len(nums) // 2
        dct = {}
        for el in nums:
            if not el in dct:
                dct[el] = 1
            else:
                dct[el] += 1
            if dct[el] > mintimes:
                return el
        return None