

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def rotateRight(self, head, k):
        if head is None:
            return head

        curr = head
        third = head

        # no of links
        n = 0
        while head.next:
            n += 1
            head = head.next

        k = k % (n + 1)

        if k == 0:
            return curr

        head.next = curr

        for i in range(n + 1 - k):
            curr = third
            third = third.next

        curr.next = None

        return third


