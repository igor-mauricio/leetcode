#
# @lc app=leetcode id=2 lang=python3
#
# [2] Add Two Numbers
#

# @lc code=start
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
from typing import Optional


class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        result = ListNode((l1.val + l2.val) % 10)
        current_result = result
        remainder = int((l1.val + l2.val - (l1.val + l2.val) % 10)/10)
        l1 = l1.next
        l2 = l2.next
        while True:
            if l1 is None and l2 is None:
                if remainder > 0:
                    current_result.next = ListNode(remainder)
                break
            if l1 is None:
                current_result.next = ListNode((l2.val + remainder)% 10)
                remainder = int((l2.val + remainder - (l2.val + remainder) % 10)/10)
            elif l2 is None:
                current_result.next = ListNode((l1.val + remainder)% 10)
                remainder = int((l1.val + remainder - (l1.val + remainder) % 10)/10)
            else:
                current_result.next = ListNode((l1.val + l2.val + remainder) % 10)
                remainder = int((l1.val + l2.val + remainder - (l1.val + l2.val + remainder) % 10)/10)
            if l1 is not None:
                l1 = l1.next
            if l2 is not None:
                l2 = l2.next
            current_result = current_result.next
        return result

if __name__ == "__main__":
    result = Solution().addTwoNumbers(ListNode(9, ListNode(9, ListNode(9, ListNode(9,ListNode(9,ListNode(9,ListNode(9))))))), ListNode(9, ListNode(9, ListNode(9,ListNode(9)))))
    while True:
        print(result.val)
        if result.next == None:
            break
        result = result.next
# @lc code=end

