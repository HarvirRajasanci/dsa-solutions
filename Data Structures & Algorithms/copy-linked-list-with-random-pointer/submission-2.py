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

        curr = head
        while curr:
            oldToNew.get(curr).next = oldToNew.get(curr.next)
            oldToNew.get(curr).random = oldToNew.get(curr.random)
            curr = curr.next
            
        return oldToNew.get(head)