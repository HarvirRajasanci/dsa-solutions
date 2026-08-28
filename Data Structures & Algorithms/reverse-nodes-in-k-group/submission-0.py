# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        length = 0
        curr = head
        while curr:
            length += 1
            curr = curr.next

        groups = length // k
        curr = head
        tail = new_head = None

        while groups:
            prev = None
            curr_tail = curr

            for i in range(k):
                temp = curr.next
                curr.next = prev
                prev = curr
                curr = temp

            if tail:
                tail.next = prev
            tail = curr_tail

            if not new_head:
                new_head = prev

            groups -= 1

        if curr:
            tail.next = curr

        return new_head 