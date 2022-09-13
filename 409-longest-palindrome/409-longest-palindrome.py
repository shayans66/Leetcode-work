class Solution:
    def longestPalindrome(self, s: str) -> int:
        h = {}
        for e in s:
            h[e] = h.get(e,0)+1
        
        vals = sorted(list(h.values()), reverse=True)
        
        t = 0
        even = False
        for e in vals:
            if e%2==1 and not even:
                t += e
                even = True
            else:
                t += e if e%2==0 else e-1
        return t
            