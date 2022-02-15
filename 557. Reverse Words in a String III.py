class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        listString = s.split()
        for i in range(len(listString)):
            listString[i] = listString[i][::-1]
        return ' '.join(listString)