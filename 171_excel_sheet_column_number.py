class Solution:
    def titleToNumber(self, s: str) -> int:
        
        result = 0
        for i in range(len(s)):
            result+= (26**(len(s)-i-1))*(ord(s[i])-64)
        return result
        