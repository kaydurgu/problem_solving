# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        helperA = headA
        helperB = headB
        if headA and headB:
            helperA = headA
            helperB = headB
            while helperA != helperB:
                #print(helperA.val ,helperB.val)
                helperA = helperA.next if helperA else headB
                helperB = helperB.next if helperB else headA
            return helperA