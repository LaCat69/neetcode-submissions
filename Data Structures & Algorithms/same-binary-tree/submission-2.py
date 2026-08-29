# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if p and q and p.val != q.val:
            return False
        if not p and not q:
            return True
        if not p or not q:
            return False

        q1 = deque([p])
        q2 = deque([q])

        while q1 and q2:
            node1 = q1.popleft()
            node2 = q2.popleft()
            if (node1 and node1.left) and (node2 and node2.left):
                if node1.left.val != node2.left.val:
                    return False
                q1.append(node1.left)
                q2.append(node2.left)
            elif (node1 and node1.left) or (node2 and node2.left):
                return False
            if (node1 and node1.right) and (node2 and node2.right):
                if node1.right.val != node2.right.val:
                    return False
                q1.append(node1.right)
                q2.append(node2.right)
            elif (node1 and node1.right) or (node2 and node2.right):
                return False
            
        return True