class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l,r=0,len(nums)-1
        while l<r:
            m = l+(r-l)//2
            if nums[m] > nums[r]:
                l=m+1
            else:
                r=m
        
        smlst = l
        l,r=0,len(nums)-1
        
        # right
        if target >= nums[smlst] and target <= nums[r]:
            l = smlst
        else:
            r = smlst-1 if smlst-1>=0 else 0
            
        return self.bin_search(nums, l, r, target)
    
    def bin_search(self, arr,l,r,x):
        while(l<=r):
            m = l + (r-l)//2
            
            if x < arr[m]:
                r = m-1
            elif arr[m] < x:
                l = m+1
            else:
                return m
        return -1