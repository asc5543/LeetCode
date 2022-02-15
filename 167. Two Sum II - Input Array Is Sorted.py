class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        rightIndex = 0
        leftIndex = len(numbers)-1
        while numbers[rightIndex] + numbers[leftIndex] != target:
            if numbers[rightIndex] + numbers[leftIndex] > target:
                leftIndex -= 1
            else:
                rightIndex += 1
        return [rightIndex+1, leftIndex+1]