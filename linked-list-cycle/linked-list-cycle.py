# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        if not head:
            return False
        
        one_time = two_time = head
        while True:
#             if head and head.next:
#                 one_time = one_time.next
#                 two_time = two_time.next
#                 if head.next.next:
#                     two_time = two_time.next
#                 else: return False
#             else: return False
            
#             if one_time.val == two_time.val and one_time == two_time:
#                 return True

            if one_time.next and two_time.next and two_time.next.next:
                one_time = one_time.next
                two_time = two_time.next.next
            else: return False
            if one_time == two_time and one_time.val == two_time.val:
                return True
                
        return False
            