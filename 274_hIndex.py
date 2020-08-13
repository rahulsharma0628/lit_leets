class Solution:
    def hIndex(self, citations: List[int]) -> int:
        
        n = len(citations)
        temp = [0]*(n+1)
        
        for i in range(n):
            if citations[i]>n:
                temp[n] += 1
            else:
                temp[citations[i]]+=1
        print(temp)
        
        sum_ = 0
        
        for i in range(n, -1, -1):
            sum_+=temp[i]
            if sum_>=i:
                return i