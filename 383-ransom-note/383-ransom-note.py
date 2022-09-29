class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        a = Counter(ransomNote)
        b = Counter(magazine)
        
        # a subset of b
        print(a,b)
        for e in a:
            for i in range(a[e]):
                b[e] -= 1
                if b[e]<0:
                    return False
        return True
