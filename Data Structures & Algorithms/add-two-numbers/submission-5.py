# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        head = ListNode()
        current = head
        rest = 0
        while l1 and l2:
            somme = l1.val + l2.val + rest
            if somme < 10:
                current.next = ListNode(somme)
                rest = 0
            else:
                current.next = ListNode(somme % 10)
                rest = 1
            current = current.next
            l1 = l1.next
            l2 = l2.next

        while l1:
            somme = l1.val + rest
            if somme < 10:
                current.next = ListNode(somme)
                rest = 0
            else:
                current.next = ListNode(somme % 10)
                rest = 1
            l1 = l1.next
            current = current.next

        while l2:
            somme = l2.val + rest
            if somme < 10:
                current.next = ListNode(somme)
                rest = 0
            else:
                current.next = ListNode(somme % 10)
                rest = 1
            l2 = l2.next
            current = current.next

        if rest:
            current.next = ListNode(rest)

        return head.next