class Solution:
    def isPowerOfFour(self, num: int) -> bool:
        # zeroes = bin(num).split('b')[1].count('0')
        # ones = bin(num).split('b')[1].count('1')
        return num>0 and len(bin(num))%2 and not num&(num-1)