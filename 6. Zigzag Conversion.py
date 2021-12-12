class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        if numRows == 1:
            return s
        
        # Partition will be numRows*2-2
        dictSubString = {}
        strResult = ""
        # init dict
        for i in range(numRows):
            dictSubString[i+1] = ""
            
        for i in range(len(s)):
            index = (i+1) % (numRows*2-2)
            if index == 0:
                index = numRows*2-2
            if index > numRows:
                dictSubString[numRows-(index-numRows)] = dictSubString[numRows-(index-numRows)] + s[i]
            else:
                dictSubString[index] = dictSubString[index] + s[i]
                
        for i in range(numRows):
            strResult = strResult + dictSubString[i+1]
        
        return strResult