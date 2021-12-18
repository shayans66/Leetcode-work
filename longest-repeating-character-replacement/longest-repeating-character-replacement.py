class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = {}
        l,res = 0,0
        
        for r in range(len(s)):
            # update hashmap
            count[s[r]] = 1 + count.get(s[r],0)
            # if windowlen-maxfreq > k, slide window
            if r-l+1 - max(count.values()) > k:
                count[s[l]] -= 1
                l += 1
            # update res (amt of replacements)
            res = max(res,r-l+1)
        return res