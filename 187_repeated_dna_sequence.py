class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        
        if len(s)<=10:
            return [] 
        
        dnaSequenceTen = []
        result = []
        
        for i in range(len(s) - 9):
            dnaSequenceTen.append(s[i:i+10])
        print(dnaSequenceTen)
            
        countSequence = collections.Counter(dnaSequenceTen)
        
        for k,v in countSequence.items():
            if v>1:
                result.append(k)
        return result 