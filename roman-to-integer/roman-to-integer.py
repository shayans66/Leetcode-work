class Solution:
    def romanToInt(self, s: str) -> int:
        
        T = {
        'I':             1,
        'V':             5,
        'X':            10,
        'L':           50,
        'C':          100,
        'D':         500,
        'M':        1000,
        }
        
        # for i in range(len(s)):
        #    if s[i] < s[i+1]:
        #         z -= 
        
        largestLet = res = 0
        
        
        for i in range(len(s)-1, -1, -1):
            l = s[i]
            if T[l] < largestLet:
                res -= T[l]
            else:
                res += T[l]
                largestLet = T[l]
                
        return res if res >= 0 else 0