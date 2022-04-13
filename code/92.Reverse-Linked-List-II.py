# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        if left == 1:
            return self.reverseN(head, right)
        head.next = self.reverseBetween(head.next, left - 1, right - 1)
        return head
           
    succ = None
    def reverseN(self, head, n):
        if n == 1:
            self.succ = head.next
            return head
        last = self.reverseN(head.next, n-1)
        head.next.next = head
        head.next = self.succ
        return last   