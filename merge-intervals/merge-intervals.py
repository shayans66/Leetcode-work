class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
#         intervals = sorted(intervals, key= lambda x: x[0])
        
#         i=0
#         while i < len(intervals)-1:
#             if intervals[i][1] >= intervals[i+1][0]:
#                 # overlapped[i]=overlapped[i+1] = 1
#                 # mark the inner elem
                
#                 tmp = intervals[i] + intervals[i+1]
#                 intervals[i] = [min(tmp), max(tmp)]
#                 del intervals[i+1]
#                 continue
#             i+=1
            
                
#         return intervals

        out = []
        for i in sorted(intervals, key=lambda i: i[0]):
            if out and i[0] <= out[-1][1]:
                out[-1][1] = max(out[-1][1], i[1])
            else:
                out += i,
        return out