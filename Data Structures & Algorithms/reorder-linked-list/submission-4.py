# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        list2 = slow.next
        slow.next = prev = None

        while list2:
            temp = list2.next
            list2.next = prev
            prev = list2
            list2 = temp

        list1, list2 = head, prev
        while list1 and list2:
            n1, n2 = list1.next, list2.next

            list1.next = list2
            list2.next = n1

            list1, list2 = n1, n2



