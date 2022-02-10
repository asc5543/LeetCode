class Solution(object):
    def sortedSquares(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        listMinusSquare = []
        listNatureSquare = []
        for num in nums:
            if num < 0:
                listMinusSquare.append(num * num)
            elif num >= 0:
                listNatureSquare.append(num * num)
        listMinusSquare = listMinusSquare[::-1]
        listSquare = []
        indexMinus, indexNature = 0, 0
        while indexMinus < len(listMinusSquare) and indexNature < len(listNatureSquare):
            if listMinusSquare[indexMinus] <= listNatureSquare[indexNature]:
                listSquare.append(listMinusSquare[indexMinus])
                indexMinus += 1
            else:
                listSquare.append(listNatureSquare[indexNature])
                indexNature += 1               
        while indexMinus < len(listMinusSquare):
            listSquare.append(listMinusSquare[indexMinus])
            indexMinus += 1
        while indexNature < len(listNatureSquare):
            listSquare.append(listNatureSquare[indexNature])
            indexNature += 1      
        return listSquare