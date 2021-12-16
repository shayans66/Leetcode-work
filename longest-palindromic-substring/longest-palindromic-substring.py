class Solution:
    def longestPalindrome(self, s: str) -> str:
        # l=0
        # n=0
        # for i in range(len(s)):
        #     for j in range(i+1, len(s)+1):
        #         if s[i:j] == s[i:j][::-1] and len(s[i:j])>n:
        #             l = s[i:j]
        #             n = len(s[i:j])
        # return l
        
        res,resLen = '',0
        # l,r = 0, len(s)-1
        # print(s)
        for i in range(len(s)):
            #odd
            l,r = i,i
            # print(l,r,s[l],s[r])
            while l>=0 and r<len(s) and s[l]==s[r]:
                if len(s[l:r+1]) > resLen:
                    resLen = len(s[l:r+1])
                    res = s[l:r+1]
                l-=1
                r+=1
                # print(l,r)
            #even
            l,r = i,i+1
            while l>=0 and r<len(s) and s[l]==s[r]:
                if len(s[l:r+1]) > resLen:
                    resLen = len(s[l:r+1])
                    res = s[l:r+1]
                l-=1
                r+=1
        return res