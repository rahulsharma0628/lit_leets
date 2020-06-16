# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        
        if not root: return []

        res = []
        stack = [(root, False)]
        
        
        while stack:
            curr, noLeft = stack.pop()
            if curr:
                if not noLeft:
                    stack.append((curr.right, False))
                    stack.append((curr, True))
                    stack.append((curr.left, False))
                else:
                    res.append(curr.val)
        return res
                
            

#         res = []
#         self.helper(root, res)
#         return res
    
#     def helper(self, root, res):
#         if root != None:
#             if root.left!=None:
#                 self.helper(root.left,res)
                
#             res.append(root.val)
            
#             if root.right!=None:
#                 self.helper(root.right, res)