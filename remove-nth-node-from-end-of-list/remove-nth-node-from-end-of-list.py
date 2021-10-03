# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        cur = head
        ln=0
        while cur:
            end = cur
            ln+=1
            cur = cur.next
            
        place = ln - n + 1
        # print(ln,n,place)
        i = 1
        prev,cur = None,head
        while cur:
            # print(i,prev.val,cur.val)
            # print(f'i:{i}==n:{n}?')
            if i == place:
                if prev is None:
                    return head.next
                prev.next = cur.next
                
                return head
            i += 1
            prev,cur = cur, cur.next
            
        
        return head