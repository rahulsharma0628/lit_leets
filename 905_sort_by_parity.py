class Solution:
    def sortArrayByParity(self, A: List[int]) -> List[int]:
        i, j = 0, len(A) -  1
        
        while i<=j:
            if self.isEven(A[i]):
                i+=1
                continue
            elif not self.isEven(A[j]):
                j-=1
                continue
            else:
                A[i], A[j] = A[j], A[i]
        return A
                
       
    def isEven(self, num):
        return True if num%2==0 else False
    