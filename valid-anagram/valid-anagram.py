from collections import defaultdict
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # dt1 = dt2 = defaultdict(lambda: 0)
        dt1= {}
        dt2 = dict()
        
        if len(s)!=len(t):
            return False
        for i in range(len(s)):
            dt1[s[i]] = dt1.get(s[i], 0) + 1
            dt2[t[i]] = dt2.get(t[i], 0) + 1
        print(dt1,dt2)
        return dt1==dt2