# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        # retlist = ListNode(0)
        
        dummy = ListNode(0)
        
        first, second = l1, l2
        cur = dummy
        
        while first or second:
            if (not second) or (first and second and first.val <= second.val):
                cur.next = cur = ListNode(first.val)
                first = first.next
            else:
                cur.next = cur = ListNode(second.val)
                second = second.next
            
        
        return dummy.next