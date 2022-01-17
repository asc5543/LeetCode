class Solution(object):
    def wordPattern(self, pattern, s):
        """
        :type pattern: str
        :type s: str
        :rtype: bool
        """
        dictBijectionPattern = {}
        dictBijectionS = {}
        listString = s.split(" ")
        if not len(pattern) == len(listString):
            return False
        if not len(set(pattern)) == len(set(listString)):
            return False
        for i in range(len(pattern)):
            p = pattern[i]
            if dictBijectionPattern.has_key(p):
                if not dictBijectionPattern[p] == listString[i]:
                    return False
            else:
                dictBijectionPattern[p] = listString[i]

        return True