# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        
        q = collections.deque([root, None])
        
        levelOrder = []
        levelValues = []
        
        while q:
            node = q.popleft()
            print(node)
            if node is None:
                levelOrder.append(levelValues)
                print(levelOrder)
                levelValues = []
                if q: q.append(None)
            else:
                levelValues.append(node.val)
                if node.left: q.append(node.left)
                if node.right: q.append(node.right)
                print(q)
                # print(node)
        return levelOrder