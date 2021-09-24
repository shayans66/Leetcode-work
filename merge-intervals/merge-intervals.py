class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals = sorted(intervals, key= lambda x: x[0])
        
        i=0
        print(intervals)
        while i < len(intervals)-1:
            if intervals[i][1] >= intervals[i+1][0]:
                # overlapped[i]=overlapped[i+1] = 1
                # mark the inner elem
                
                tmp = intervals[i] + intervals[i+1]
                intervals[i] = [min(tmp), max(tmp)]
                del intervals[i+1]
                continue
            i+=1
            
                
        return intervals