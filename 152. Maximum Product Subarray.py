class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        intMaxProduct = 1
        intMinProduct = 1
        intResult = nums[0]
        for num in nums:
            value = (num, num * intMaxProduct, num * intMinProduct)
            intMaxProduct = max(value)
            intMinProduct = min(value)
            intResult = max(intResult, intMaxProduct)

                
        return intResult