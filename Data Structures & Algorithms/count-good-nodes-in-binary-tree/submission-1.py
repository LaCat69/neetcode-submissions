# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        res = 0
        q = deque([(root, float("-inf"))])

        while q:
            node, prev_max = q.popleft()
            if node.val >= prev_max:
                res += 1
            
            if node.left:
                q.append((node.left, max(prev_max, node.val)))

            if node.right:
                q.append((node.right, max(prev_max, node.val)))

        return res