class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        arr = list(range(1, len(nums) + 1))
        hm = {}
        for n in arr:
            hm[n] = 0
        print(hm)
        for n in nums:
            if n in hm.keys():
                del hm[n]
            
            
        return hm.keys()