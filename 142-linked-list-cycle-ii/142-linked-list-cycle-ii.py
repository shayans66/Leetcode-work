# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        t,h = head,head
        intsct = None
        while t and h and h.next:
            t = t.next
            h = h.next.next
            if t == h:
                intsct = t
                break
        
        if not intsct:
            return None
        
        p = head
        
#        while p and intsct:
#            p = p.next
#            intsct = intsct.next
#            if p == intsct:
#                return p
#        return None
        
        ptr1 = head
        ptr2 = intsct
        while ptr1 != ptr2:
            ptr1 = ptr1.next
            ptr2 = ptr2.next

        return ptr1