class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        
        n = len(digits)
        num = 0
        for i in range(len(digits)):
            num+= digits[-i-1]*(10**i)
        
        num = num + 1
        result = []
        num_s = str(num) 
        for i in num_s:
            result.append(int(i))
        return result

#Converted digits in a number --> then number into str for iteration and appended int casted string to result list 