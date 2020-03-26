class Solution:
    def hammingWeight(self, n: int) -> int:        
        count = 0
        while n:
            count+=n%2
            n = n//2
        return count

    def hammingWeight_alternate(self, n: int) -> int:    
        count = 0 
        s_n = '{0:08b}'.format(n)
        for num in s_n:
            if num == '1':
                count+=1
        return count