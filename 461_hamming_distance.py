class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
                
        result = 0
        
        x_bin = bin(x).split('b')[1]
        y_bin = bin(y).split('b')[1]
        
        size = max(len(x_bin), len(y_bin))
        diff = abs(len(x_bin) - len(y_bin))
        
        if len(x_bin)<=len(y_bin):
            x_bin = '0'*diff+x_bin
        else:
            y_bin = '0'*diff+y_bin
            
        for i in range(size):
            if x_bin[i]!=y_bin[i]:
                result+=1
        return result