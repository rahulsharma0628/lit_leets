class Solution:
    def isPrefixOfWord(self, sentence: str, searchWord: str) -> int:
        
        for i,w in enumerate(sentence.split(), 1):
            if w.startswith(searchWord):
                return i
        return -1

    def isPrefixOfWordAlternate(self, sentence: str, searchWord: str) -> int:

        words = sentence.split()
        print(words)
        
        for i in range(len(words)):
            if words[i].startswith(searchWord):
                return i+1
        return -1
        