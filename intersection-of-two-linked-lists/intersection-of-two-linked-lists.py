# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        
        
        nodeA = headA
        nodeB = headB
        while nodeA or nodeB:
            if nodeA:
                if hasattr(nodeA, 'passed'):
                    return nodeA
                else:
                    nodeA.passed = True
                    nodeA = nodeA.next
                    
            if nodeB:
                if hasattr(nodeB, 'passed'):
                    return nodeB
                else:
                    nodeB.passed = True
                    nodeB = nodeB.next
        return None
        