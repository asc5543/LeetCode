class StreamChecker(object):

    def __init__(self, words):
        """
        :type words: List[str]
        """
        self.listWord = list(set(words))
        self.strStream = ""
        
        # Use dict to record last word and map to word list
        self.lenWord, self.dictWord = self.initWordList()

    def query(self, letter):
        """
        :type letter: str
        :rtype: bool
        """
        self.strStream = self.strStream+letter
        if len(self.strStream) > self.lenWord:
            self.strStream = self.strStream[(len(self.strStream) - self.lenWord):]
            
        # No match last word, no query
        if not letter in self.dictWord.keys():
            return False
        
        for word in self.dictWord[letter]:
            if word == self.strStream[len(self.strStream) - len(word):]:
                return True
        return False
     
    def initWordList(self):
        dictWord = {}
        intLength = 0
        for word in self.listWord:
            intLength = max(len(word), intLength)
            if not word[-1] in dictWord.keys():
                dictWord[word[-1]] = []
            dictWord[word[-1]].append(word)
        return intLength, dictWord


# Your StreamChecker object will be instantiated and called as such:
# obj = StreamChecker(words)
# param_1 = obj.query(letter)