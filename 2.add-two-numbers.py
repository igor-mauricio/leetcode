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
        sum_l1 = 0
        while l1.next != None:
            sum_l1 *= 10
            sum_l1 += l1.val
            l1 = l1.next
        sum_l2 = 0
        while l2.next != None:
            sum_l2 *= 10
            sum_l2 += l2.val
            l2 = l2.next
        sum = sum_l1 + sum_l2
        result = ListNode()
        current_node = result
        while sum > 0:    
            current_node.val = int(sum % 10)
            result.next = ListNode()
            current_node = result.next
            sum = (sum - sum%10)/ 10
        return result
        
# @lc code=end

