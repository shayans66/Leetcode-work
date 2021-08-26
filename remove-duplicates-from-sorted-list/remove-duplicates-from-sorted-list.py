# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
#         cur = head
#         newValPtr = head and head.val
#         while cur:
#             if newValPtr != cur.val:
#                 newPtr = cur.val
            
#             if newValPtr != cur and 
            
#             cur = cur.next
            
        if not head or not head.next:
            return head
        while head.next and head.val == head.next.val:
            head.next = head.next.next
        
        slow = fast = head.next

        while fast:
            if fast == slow: fast = fast.next
            elif slow.val == fast.val:
                slow.next = fast = fast.next
            else:
                slow = fast
        return head