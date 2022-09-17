class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        def dist(x, y):
            return abs(x[0]-y[0]) ** 2 + abs(x[1]-y[1]) ** 2
        
        pts = []
        for p in points:
            pts.append([dist(p, [0,0]), p[0], p[1]])
        
        heapq.heapify(pts)
        
        res = []
        
        for i in range(k):
            res.append(heapq.heappop(pts)[1:]) 
        return res
        