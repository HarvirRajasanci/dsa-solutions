# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        curr = head

        length = 0
        while curr:
            curr = curr.next
            length += 1

        if length - n == 0:
            return head.next

        length = length - n - 1

        curr = head
        for _ in range(length):
            curr = curr.next

        curr.next = curr.next.next

        return head