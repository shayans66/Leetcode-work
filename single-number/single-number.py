class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        # x ^ x = 0
        # x ^ 0 = x
        
        # (x ^ x) ^ (a ^ a) ^ (b ^ b) ^ c =
        # 0 ^ 0 ^ 0 ^ c = c
        
        sol = 0
        for n in nums:
            sol = sol ^ n
        return sol