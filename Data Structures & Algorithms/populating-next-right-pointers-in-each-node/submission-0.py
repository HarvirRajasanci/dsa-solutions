"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        if not root:
            return root
        
        q = deque([root])
        while q:
            size = len(q)
            prev = None
            for i in range(size):
                node = q.popleft()

                if prev:
                    prev.next = node
                prev = node

                q.append(node.left) if node.left else None
                q.append(node.right) if node.right else None
            prev = None              
        return root