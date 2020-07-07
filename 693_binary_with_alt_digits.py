class Solution:
    def hasAlternatingBits(self, n: int) -> bool:
        
        return (n & (n>>1))==0 and (n & (n>>2))==(n>>2)
        
        # n_bit = bin(n).split('b')[1]
        # print(n_bit)
        # for i in range(1,len(n_bit)):
        #     if n_bit[i]==n_bit[i-1]:
        #         return False
        # return True
                