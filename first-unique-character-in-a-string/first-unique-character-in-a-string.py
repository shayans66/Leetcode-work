class Solution:
    def firstUniqChar(self, s: str) -> int:
        dt = dict()
        for ch in s:
            if ch in dt:
                dt[ch]+=1
            else:
                dt[ch]=1
        for i,ch in enumerate(s):
            if dt[ch] == 1:
                return i
        return -1