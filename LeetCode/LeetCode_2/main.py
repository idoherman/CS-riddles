# Definition for singly-linked list.

class ListNode(object):

    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    # Recursion that prints Linked List (Node)
    def __str__(self):
        if self.next is None:
            return f"{self.val}"
        return f"{self.val} => {str(self.next)}"


class Solution(object):
    def addTwoNumbers(self, l1, l2):
        l_start = ListNode(0, None)
        l_end = l_start
        above_9 = 0

        while l1 is not None or l2 is not None:
            if l1 is not None:
                l_end.val += l1.val
                l1 = l1.next

            if l2 is not None:
                l_end.val += l2.val
                l2 = l2.next

            if l_end.val > 9:
                above_9 = 1
                l_end.val -= 10

            if l1 is not None or l2 is not None or above_9 == 1:
                l_end.next = ListNode(above_9, None)
                l_end = l_end.next
                above_9 = 0

        return l_start
