class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        indexLeft = 0
        indexRight = 0
        for i in range(len(s)-1):
            indexSingleLeft, indexSingleRight = self.ExtendPalindromic(s, i, i)
            indexDoubleLeft, indexDoubleRight = self.ExtendPalindromic(s, i, i+1)
            
            if indexDoubleRight - indexDoubleLeft > indexSingleRight - indexSingleLeft:
                if indexRight - indexLeft < indexDoubleRight - indexDoubleLeft:
                    indexLeft, indexRight = indexDoubleLeft, indexDoubleRight
            else:
                if indexRight - indexLeft < indexSingleRight - indexSingleLeft:
                    indexLeft, indexRight = indexSingleLeft, indexSingleRight
                
        return s[indexLeft:indexRight+1]
        
        
    def ExtendPalindromic(self, s, indexLeft, indexRight):
        while (indexLeft >= 0 and indexRight < len(s)) and (s[indexLeft] == s[indexRight]):
            indexLeft = indexLeft - 1
            indexRight = indexRight + 1
        return indexLeft+1, indexRight-1