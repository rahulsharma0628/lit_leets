"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def maxDepth(self, root: 'Node') -> int:
        if root is None:
            return 0
        
        maxDepth = 0
        for child in root.children:
            maxDepth = max(maxDepth, self.maxDepth(child))
        return maxDepth+1        
            