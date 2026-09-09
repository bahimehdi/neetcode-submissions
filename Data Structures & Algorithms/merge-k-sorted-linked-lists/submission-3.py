# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        fullLists = []
        for i in range(len(lists)):
            if lists[i]:
                fullLists.append(lists[i])
        k = len(fullLists)
        if k == 1:
            return fullLists[0]
        elif k == 2:
            return self.mergeTwoLists(fullLists[0], fullLists[1])
        elif k >= 3:
            i = 0
            nextRound = []
            while i + 1 < k:
                nextRound.append(self.mergeTwoLists(fullLists[i], fullLists[i+1]))
                i += 2
            if i < k:
                nextRound.append(fullLists[i])
            return self.mergeKLists(nextRound)
        return None

    # re-using two sorted llists merge
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        L1cur, L2cur = list1, list2
        tail = ListNode()
        merged = tail
        while L1cur is not None and L2cur is not None:
            if L1cur.val > L2cur.val:
                tail.next = L2cur
                tail = L2cur
                L2cur = L2cur.next
            else:
                tail.next = L1cur
                tail = L1cur
                L1cur = L1cur.next
        if L1cur is not None:
            tail.next = L1cur
            tail = L1cur
        if L2cur is not None:
            tail.next = L2cur
            tail = L2cur
        return merged.next