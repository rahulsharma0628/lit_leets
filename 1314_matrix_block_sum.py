class Solution:
    def matrixBlockSum(self, mat: List[List[int]], K: int) -> List[List[int]]:

        #1 - FUNC: for each position get the appropriate collection of element indices
        #2 - get sum at all position and save into an answer matrix
        ans = [[0]*len(mat[0]) for _ in range(len(mat))]
        print(ans)
        
        for i in range(len(mat)):
            for j in range(len(mat[0])):
                ans[i][j] = self.sumOfValidElements(i,j,mat,K)
        
        # print(self.sumOfValidElements(2,2,mat,K))
        return ans
        
    def sumOfValidElements(self,i,j,mat,K):
        sums = 0
        for a in range(i-K,i+K+1):
            for b in range(j-K, j+K+1):
                if a<0 or b<0 or a>len(mat)-1 or b>len(mat[0])-1:
                    sums+=0
                else:
                    sums+=mat[a][b]
        return sums
        
#### This solution gives exceed time limit for bigger matrix       