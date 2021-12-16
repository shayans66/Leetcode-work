class Solution:
    def countSubstrings(self, s: str) -> int:
        tot = 0
        for i in range(len(s)):
            l,r = i,i
            while l>=0 and r<len(s) and s[l]==s[r]:
                # if len(s[l:r+1]) > resLen:
                #     resLen = len(s[l:r+1])
                #     res = s[l:r+1]
                tot += 1
                l-=1
                r+=1
                # print(l,r)
            #even
            l,r = i,i+1
            while l>=0 and r<len(s) and s[l]==s[r]:
                tot+=1
                l-=1
                r+=1
        return tot