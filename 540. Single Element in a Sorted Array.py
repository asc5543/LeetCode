class Solution(object):
    def singleNonDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        left = 0
        right = len(nums)-1
        while left < right:
            mid = (left+right) // 2
            if nums[mid] == nums[mid-1]:
                subleft = mid-left+1
                if subleft % 2 == 0:
                    left = mid + 1
                else:
                    right = mid
                    
            elif nums[mid] == nums[mid+1]:
                subright = right - mid + 1
                if subright % 2 == 0:
                    right = mid - 1
                else:
                    left = mid
            else:
                return nums[mid]
            
        return nums[left]