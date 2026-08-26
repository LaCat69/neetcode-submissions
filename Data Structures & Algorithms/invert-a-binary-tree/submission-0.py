# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return
        next_left = root.left
        next_right = root.right
        root.left = self.invertTree(next_right)
        root.right = self.invertTree(next_left)

        return root