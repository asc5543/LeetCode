class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        boolHasZero = False
        intTotalProduct = 1
        # No product zero
        for i in range(len(nums)):    
            # Skip zero part
            if nums[i] == 0:
                # Not first zero, all index will become zero
                if boolHasZero:
                    return [0] * len(nums)
                else:
                    boolHasZero = True
            
            else:
                intTotalProduct = intTotalProduct * nums[i]
        
        arrAnswer = []
        for i in range(len(nums)):
            if boolHasZero:
                if nums[i] == 0:
                    arrAnswer.append(intTotalProduct)
                else:
                    arrAnswer.append(0)
                    
            else:
                arrAnswer.append(intTotalProduct/nums[i])
        return arrAnswer