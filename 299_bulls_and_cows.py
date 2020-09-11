class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        
        bulls = 0
        cows = 0
        
        secretHash = collections.Counter(secret)
        
        for i,ch in enumerate(guess):
            if ch in secret:
                if ch == secret[i]:
                    bulls += 1
                    cows-= int(secretHash[ch]<=0)
                elif secretHash[ch]>0:                    
                    cows+=1
                secretHash[ch]-= 1
        
        return str(bulls)+'A'+str(cows)+'B'