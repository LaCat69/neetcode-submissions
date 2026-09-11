# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        res = root.val

        def dfs(node):
            if not node:
                return 0
            nonlocal res
            
            left_max = dfs(node.left)
            right_max = dfs(node.right)
            
            left_max = max(left_max, 0)
            right_max = max(right_max, 0)

            res = max(res, node.val + left_max + right_max)
            
            return max(left_max, right_max) + node.val
        
        dfs(root)
        return res