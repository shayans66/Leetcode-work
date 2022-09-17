class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        nums = [-a for a in nums]
        heapq.heapify(nums)
        
        res = []
        for i in range(k):
            res.append(heapq.heappop(nums))
        
        print(res)
        return -res[-1]
                       