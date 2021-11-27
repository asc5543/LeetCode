class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums = sorted(nums)
        dictHasSeen = {}
        listResult = []
        i = 0
        while i < len(nums):
            if nums[i] > 0:
                break
            if not dictHasSeen.has_key(nums[i]):
                target = 0 - nums[i]            
                dictHasSeen[nums[i]] = target
                dictMap = {}
                j = i + 1
                while j < len(nums):
                    complement = target - nums[j];
                    if dictMap.has_key(complement):
                        result = sorted([nums[i]] + [nums[j]] + [complement])
                        listResult.append(result)
                        while i < len(nums)-1 and nums[i] == nums[i+1]:
                            i += 1
                        while j < len(nums)-1 and nums[j] == nums[j+1]:
                            j += 1
                    else:
                        dictMap[nums[j]] = j
                    j += 1
            i += 1
        return sorted(listResult)