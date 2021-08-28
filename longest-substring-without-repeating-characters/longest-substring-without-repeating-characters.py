class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
#         idxs = []
#         char_idxs = {}
#         maxlen = 0
        
#         for i,num in enumerate(s):
            
        map = {}
        m = 0
        l = 0
        for i,ch in enumerate(s):
            # if we seen ch before, update left ptr to be 1 plus old index
            # then update new index in dict, then update max
            if ch in map:
                l = max(l, map[ch]+1)
            map[ch] = i
            m = max(m, i-l+1)
        return m
            