# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        prehead = ListNode(-1)
        
        cur = prehead
        
        a, b = l1, l2
        
        while a and b:
            if a.val < b.val:
                cur.next = ListNode(a.val)
                a = a.next
            else:
                cur.next = ListNode(b.val)
                b = b.next
            cur = cur.next
        
        cur.next = a if a else b
        
        return prehead.next
                