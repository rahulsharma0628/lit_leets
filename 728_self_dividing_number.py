class Solution:
    def selfDividingNumbers(self, left: int, right: int) -> List[int]:
        
        return [num for num in range(left,right+1) if self.isSelfDividingCriteria(num)]
        
    def isSelfDividingCriteria(self, num):
        digits = [int(ch) for ch in str(num)]
        # print(digits)
        if not self.noZeroDigits(num):
            return False
        for digit in digits:            
            if (num%digit)!= 0:
                return False
        return True
    
    def noZeroDigits(self, num):
        digits = [int(ch) for ch in str(num)]
        if 0 in digits:
            return False
        return True