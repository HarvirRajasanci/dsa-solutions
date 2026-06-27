# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        fast = slow = head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next

        second = slow.next
        slow.next = prev = None

        while second:
            temp = second.next
            second.next = prev
            prev = second
            second = temp

        first, second = head, prev
        while first and second:
            n1, n2 = first.next, second.next

            first.next = second
            second.next = n1
            first, second = n1, n2

        