"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        map = {}

        curr = head
        while curr:
            map[curr] = Node(curr.val)
            curr = curr.next

        curr = head
        while curr:
            node = map[curr]
            node.next = map.get(curr.next)
            node.random = map.get(curr.random) 
            curr = curr.next

        return map[head] if head else None