# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        slow = fast = head
        nodeNumber = 0
        
        while fast:
            fast = fast.next
            if(nodeNumber > n):
                slow = slow.next
            nodeNumber += 1

        if(nodeNumber == n):
            head = head.next
        elif slow.next: 
            slow.next = slow.next.next
        elif(slow == head):
            head = head.next
        return head