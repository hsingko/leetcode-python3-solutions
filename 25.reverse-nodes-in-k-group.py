#
# @lc app=leetcode id=25 lang=python3
#
# [25] Reverse Nodes in k-Group
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        new_head = None
        tail = None
        while head:
            stack = []
            while len(stack) < k:
                stack.append(head)
                head = head.next
            while len(stack) == k:
                pass
            head = head.next
        tail.next = None
        return new_head
# @lc code=end

