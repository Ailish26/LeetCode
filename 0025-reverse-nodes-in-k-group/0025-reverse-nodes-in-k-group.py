# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head, k):
        def reverse(group_head, prev_tail, k):
            prev_node = None
            curr_node = group_head
            count = 0
            while count < k:
                next_node = curr_node.next
                curr_node.next = prev_node
                prev_node = curr_node
                curr_node = next_node
                count += 1
            if prev_tail:
                prev_tail.next = prev_node
            return group_head, curr_node

        nodes_seen = 0
        current = head
        final_head = head
        next_group_head = head
        prev_group_tail = None
        while current:
            nodes_seen += 1
            if nodes_seen == k:
                final_head = current
            if nodes_seen % k == 0:
                prev_group_tail, next_group_head = reverse(
                    next_group_head, prev_group_tail, k
                )
                current = next_group_head
            else:
                current = current.next
        prev_group_tail.next = next_group_head
        return final_head