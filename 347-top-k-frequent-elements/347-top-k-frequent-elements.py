class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        h = {}
        for e in nums:
            h[e]=h.get(e,0)+1
#        freq = list(h.values())
        freq = [[-v,k] for k,v in h.items()]
        print(freq)
        heapq.heapify(freq)
        
        res=[]
        for i in range(k):
            v,k = heapq.heappop(freq)
            res.append(k)
        return res
            