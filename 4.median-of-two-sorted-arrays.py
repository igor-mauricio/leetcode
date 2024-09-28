#
# @lc app=leetcode id=4 lang=python3
#
# [4] Median of Two Sorted Arrays
#
# https://leetcode.com/problems/median-of-two-sorted-arrays/description/
#
# algorithms
# Hard (41.53%)
# Likes:    28742
# Dislikes: 3229
# Total Accepted:    2.9M
# Total Submissions: 6.9M
# Testcase Example:  '[1,3]\n[2]'
#
# Given two sorted arrays nums1 and nums2 of size m and n respectively, return
# the median of the two sorted arrays.
# 
# The overall run time complexity should be O(log (m+n)).
# 
# 
# Example 1:
# 
# 
# Input: nums1 = [1,3], nums2 = [2]
# Output: 2.00000
# Explanation: merged array = [1,2,3] and median is 2.
# 
# 
# Example 2:
# 
# 
# Input: nums1 = [1,2], nums2 = [3,4]
# Output: 2.50000
# Explanation: merged array = [1,2,3,4] and median is (2 + 3) / 2 = 2.5.
# 
# 
# 
# Constraints:
# 
# 
# nums1.length == m
# nums2.length == n
# 0 <= m <= 1000
# 0 <= n <= 1000
# 1 <= m + n <= 2000
# -10^6 <= nums1[i], nums2[i] <= 10^6
# 
# 
#

# @lc code=start
from typing import List


class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        total_len = len(nums1) + len(nums2)
        odd = total_len % 2
        n1_index = 0
        n2_index = 0
        final_array = []

        for i in range((total_len)//2 + 1):
            if n1_index < len(nums1) and (n2_index >= len(nums2) or nums1[n1_index] < nums2[n2_index]):
                final_array.append(nums1[n1_index])
                n1_index += 1
            else:
                final_array.append(nums2[n2_index])
                n2_index += 1

        if odd:
            return final_array[(total_len + 1)//2 -1]
        else:
            return (final_array[(total_len)//2 - 1] + final_array[(total_len)//2])/2
            
Solution().findMedianSortedArrays([], [1])
            
            
        
# @lc code=end

