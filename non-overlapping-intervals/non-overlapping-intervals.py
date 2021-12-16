class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        arr = intervals.copy()
        arr.sort(key= lambda x: x[0])
        
        def intersect(a,b):
            return (a[0]<b[1] and a[1]>b[0]) or (b[0]<a[1] and b[1]>a[0])
            
        rmvd=0
        i=0
        # ln=len(arr)
        while i<len(arr)-1:
            if intersect(arr[i],arr[i+1]):
                rmv = i+1 if arr[i][1]<arr[i+1][1] else i
                arr.pop(rmv)
                rmvd+=1
                continue
            i+=1
        return rmvd
                