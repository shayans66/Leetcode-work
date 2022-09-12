class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
            sh = {}
            th = {}
            for a,b in zip(s,t):
                if a not in sh and b not in th:
                    sh[a] = b
                    th[b] = a
                elif sh.get(a) != b or th.get(b) != a:
                    return False
            return True