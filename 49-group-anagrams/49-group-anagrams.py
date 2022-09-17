class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ans = {}
        for s in strs:
            #ans[tuple(sorted(s))] = [ans.get(tuple(sorted(s)), []), s]
            # ans[tuple(sorted(s))].append(s)
            
            ans[tuple(sorted(s))] = ans.get(tuple(sorted(s)), []) + [s]
        return ans.values()