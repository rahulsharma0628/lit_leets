# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrderBottom(self, root: TreeNode) -> List[List[int]]:
        
        que, res = [root], []        
        while que:
            nextLevel, val = [], []
            for node in que:
                if node:
                    val.append(node.val)
                    nextLevel.extend([node.left, node.right])
            if val: res.append(val)
            que = nextLevel
        return res[::-1]
                
        
        
#         q = collections.deque([root, None])
#         levelOrder = []
#         temp = []
        
#         while q:
#             node = q.popleft()
            
#             if node != None:
#                 temp.append(node.val)
#                 if node.left: q.append(node.left)
#                 if node.right: q.append(node.right)
            
#             else:
#                 levelOrder.append(temp)
#                 temp = []
#                 if q: q.append(None)
#         levelOrder.reverse()
#         return levelOrder