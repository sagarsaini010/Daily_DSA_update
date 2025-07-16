class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        low = 1
        high = len(nums)-2
        n = len(nums)
        if len(nums) == 1:
            return 0
        if nums[0] > nums[1]:
            return 0
        if nums[n-1] > nums[n-2]:
            return n-1
        while low <= high:
            mid = (low+high)//2
            if nums[mid-1] < nums[mid] and nums[mid] > nums[mid+1]:
                return mid
            elif nums[mid-1] < nums[mid]:
                low = mid+1
            else:
                high = mid -1