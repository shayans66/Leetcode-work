class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        pref = ''
        # minlen = min([len(s) for s in strs])
        
        minstr = min(strs, key=len)
        
        pref = ''
        i = 0
        for ch in minstr:
            for el in strs:
                if el[i] != ch:
                    return pref
            pref += ch
            i += 1
        return pref