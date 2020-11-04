class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        
        wordFreq = collections.Counter(words)        
        result = []
        
        sortedWordFreq = {k:v for k,v in sorted(wordFreq.items(), key=lambda x: (-x[1], x[0]))}
               
        return list(sortedWordFreq.keys())[:k]