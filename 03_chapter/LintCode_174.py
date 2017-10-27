# Definition of ListNode
class ListNode(object):

    def __init__(self, val, next=None):
        self.val = val
        self.next = next


class Solution:
    """
    @param: head: The first node of linked list.
    @param: n: An integer
    @return: The head of linked list.
    """
    def removeNthFromEnd(self, head, n):
        len = 0
        curr1 = head
        while curr1:
            len += 1
            curr1 = curr1.next

        dummy = ListNode(0)
        dummy.next = head
        head = dummy
        for i in range(len - n):
            head = head.next
        head.next = head.next.next

        return dummy.next
