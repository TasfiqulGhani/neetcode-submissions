# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        result = []
        # def dfs(node,depth):
        #     if not node:
        #         return None
            
        #     dfs(node.left,1+depth)
        #     dfs(node.right,1+depth)
        # dfs(root,0)
        # return result
        if not root:
            return []
        q = deque([root])
        result = []
        while q:
            temp = []
            for _ in range(len(q)):
                node = q.popleft()
                temp.append(node.val)
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            result.append(temp)
        return result




                












