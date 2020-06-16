# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDiffInBST(self, root: TreeNode) -> int:
        
        binaryTraverse = []        
        
        q = collections.deque([root,None])
        
        while q:
            node = q.popleft()

            if node != None:

                binaryTraverse.append(node.val)
                if node.left: q.append(node.left)
                if node.right: q.append(node.right)
                    
        binaryTraverse.sort()
        minDiff = float(inf)
        for i in range(1, len(binaryTraverse)):
            diff = binaryTraverse[i]-binaryTraverse[i-1]
            minDiff = min(minDiff, diff)
        
        return minDiff