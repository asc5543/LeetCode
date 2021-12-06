class Solution(object):
    def minCostToMoveChips(self, position):
        """
        :type position: List[int]
        :rtype: int
        """
        intOdd = 0
        intEven = 0
        for i in range(len(position)):
            if position[i] % 2 == 0:
                intEven = intEven + 1
            else:
                intOdd = intOdd + 1
        return min(intOdd, intEven)