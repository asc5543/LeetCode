class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        dictLetter = {}
        intLength = 0
        intLongest = 0
        preIndex = -1
        for i in range(0, len(s)):
            if not s[i] in dictLetter:
                dictLetter[s[i]] = i
                intLength = intLength + 1
            else: 
                lastIndex = dictLetter[s[i]]
                if lastIndex > preIndex:
                    dictLetter[s[i]] = i
                    intLength = i - lastIndex
                    preIndex = lastIndex
                else:
                    dictLetter[s[i]] = i
                    intLength = intLength + 1                   
            if intLength > intLongest:
                intLongest = intLength    
        return intLongest