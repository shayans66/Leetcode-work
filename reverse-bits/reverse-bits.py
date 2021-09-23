class Solution:
    def reverseBits(self, n):
        
        
        
        ans=0
        count = 31
        while count:
            ans += n & 1
            ans <<= 1
            n >>= 1
            count -= 1
        return ans + (n&1)