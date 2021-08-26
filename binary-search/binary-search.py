class Solution:
    def search(self, nums: List[int], target: int) -> int:
        start, end = 0, len(nums) - 1
        
        while(start <= end):
            mid = (start+end) // 2
            if(nums[mid] == target):
                return mid
            elif target < nums[mid]:
                end = mid - 1
            else:
                start = mid + 1
        return -1
        
        
    #     class Solution:
    # def search(self, nums, target):
    #     l, r = 0, len(nums) - 1
    #     while l <= r:
    #         mid = (l + r) // 2
    #         if nums[mid] < target:
    #             l = mid + 1
    #         elif nums[mid] > target:
    #             r = mid - 1
    #         else:
    #             return mid
    #     return -1