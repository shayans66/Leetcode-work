# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        l=r=''
        curl, curr =l1, l2
        while curl or curr:
            if curl:
                l += str(curl.val)
                curl = curl.next
            if curr:
                r += str(curr.val)
                curr = curr.next
        num = str(int(l[::-1]) + int(r[::-1]))[::-1]
        num = num or '0'
        
        dummyroot = cur = ListNode(-1)
        for ch in num:
            cur.next = cur = ListNode(int(ch))
        return dummyroot.next