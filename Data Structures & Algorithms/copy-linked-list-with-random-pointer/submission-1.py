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
        oldToNew = {}

        curr = head
        while curr:
            oldToNew[curr] = Node(curr.val)
            curr = curr.next
        
        for old_node, new_node in oldToNew.items():
            new_node.next = oldToNew.get(old_node.next)
            new_node.random = oldToNew.get(old_node.random)

        return oldToNew.get(head)