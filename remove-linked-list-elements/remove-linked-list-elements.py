# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
#         cur = prev = head
#         while cur:
#             if cur.val == val:
#                 cur = cur.next
#                 prev.next = cur
                
        while head and head.val == val:
            head = head.next
        
        prev = head
        cur = head and head.next
        while cur:
            if cur.val == val:
                cur = cur.next
                prev.next = cur
            else:
                cur = cur.next
                prev = prev.next
        return head