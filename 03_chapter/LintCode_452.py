# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    """
    @param: head: a ListNode
    @param: val: An integer
    @return: a ListNode
    """
    def removeElements(self, head, val):
        if head == None:
            return head
        dummy = ListNode(0)
        dummy.next = head

        prev = dummy
        while head:
            if head.val == val:
                prev.next = head.next
                head = prev
            else:
                prev = head
                head = head.next
        return dummy.next
