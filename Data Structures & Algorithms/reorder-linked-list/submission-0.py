# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        fast = slow = head

        while fast.next and fast.next.next: 
            fast = fast.next.next
            slow = slow.next

        prev, current = None, slow

        while current:
            current_next = current.next
            current.next = prev
            prev = current
            current = current_next

        first, second = head, prev
        while first and second:
            temp1, temp2 = first.next, second.next
            first.next = second
            second.next = temp1
            first, second = temp1, temp2

        print(head)