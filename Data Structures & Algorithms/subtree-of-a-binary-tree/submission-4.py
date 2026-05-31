# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        
        if subRoot is None:
            return True
        
        if root is None:
            return False
        
        if self.is_same(root,subRoot):
            return True
        
        return self.isSubtree(root.left,subRoot) or self.isSubtree(root.right,subRoot)
            


     
    def is_same(self,p,q):
        if q is None and p is None:
            return True
        
        if q is None or p is None:
            return False
        
        if not (q.val == p.val):
            return False
        
        return self.is_same(p.left,q.left) and self.is_same(p.right,q.right)

