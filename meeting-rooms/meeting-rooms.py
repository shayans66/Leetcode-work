class Solution:
    def canAttendMeetings(self, intervals: List[List[int]]) -> bool:
#         def contains(n,a):
#             l,r = a[0],a[1]
#             return n > l and n < r
        
#         def notmutex(a,b):
#             return contains(a[0],b) or contains(a[1],b) or contains(b[0],a) or contains(b[1],a)
            
#         if not intervals:
#             return True
        
#         l,r=intervals[0][0],intervals[0][1]
#         for i in range(0, len(intervals)-1):
#             if notmutex([l,r], intervals[i+1]):
#                 return False
#             tmp = [l,r]+intervals[i+1]
#             l,r = min(tmp), max(tmp)
            
#         return True

        intervals = sorted(intervals, key=lambda x: x[0])
    
        for i in range(1, len(intervals)):
            if intervals[i][0] < intervals[i-1][1]:
                return False
        return True