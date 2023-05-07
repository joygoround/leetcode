# merge-nodes-in-between-zeros/


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):
    def mergeNodes(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        modified = ListNode()
        new_head = modified
        head = head.next

        while (head.next != None):
            if head.val != 0:
                modified.val += head.val
            else:
                modified.next = ListNode()
                modified = modified.next
            head = head.next

        return new_head

# ---- reivew -------------
# runtime is too slow
# avoid using unnesseary variable.
# name varibale one_two
