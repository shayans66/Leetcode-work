class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        h,f = Counter(nums1), Counter(nums2)
        
        keys = set(h.keys()).union(f.keys())
        
        res = []
        
        for k in keys:
            freq = min(h[k], f[k])
            res.extend([k] * freq)
            
        return res