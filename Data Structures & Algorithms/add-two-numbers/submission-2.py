# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = curr = ListNode()

        remainder = 0
        while l1 or l2 or remainder:
            curr_sum = remainder

            if l1:
                curr_sum += l1.val
                l1 = l1.next
            if l2:
                curr_sum += l2.val
                l2 = l2.next

            total = curr_sum % 10
            remainder = curr_sum // 10

            curr.next = ListNode(total)
            curr = curr.next

        return dummy.next

