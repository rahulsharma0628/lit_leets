class Solution:
    
    roman_int = dict({'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000})
    
    def romanToInt(self, s: str) -> int:
        
        lst = []
        
        for ch in s:
            lst.append(self.roman_int[ch])

        result = 0
        
        for i in range(len(lst)-1):
            if lst[i]<lst[i+1]:
                result-=lst[i]
            else:
                result+=lst[i]
            
        return result+lst[-1]

# A dictionary is created for each roman literal with their associated value. 
# The logic is if the next literal has higher value then the previous then we subtracts its value else add the value.