# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None
        size = 1
        cur_node = head
        while cur_node.next:
            cur_node = cur_node.next
            size+=1
            
        req_node = size // 2 + 1
        cur_node = head
        for i in range(1, req_node+1):
            if i != req_node:
                cur_node = cur_node.next
            else:
                return cur_node
        return None