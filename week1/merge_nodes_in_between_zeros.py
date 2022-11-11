# merge-nodes-in-between-zeros/

# runtime is too slow


# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution(object):
    def mergeNodes(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        modified = ListNode(0, None)
        newhead = modified
        head = head.next

        while (head.next != None):
            if head.val != 0:
                modified.val += head.val
            else:
                new_node = ListNode(0, None)
                modified.next = new_node
                modified = modified.next
            head = head.next

        return newhead
