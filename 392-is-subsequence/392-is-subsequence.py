class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        i=0
        for e in t:
            if i<len(s) and e == s[i]:
                i += 1
        return i == len(s)
        