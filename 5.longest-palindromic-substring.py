#
# @lc app=leetcode id=5 lang=python3
#
# [5] Longest Palindromic Substring
#
# https://leetcode.com/problems/longest-palindromic-substring/description/
#
# algorithms
# Medium (34.49%)
# Likes:    29692
# Dislikes: 1816
# Total Accepted:    3.3M
# Total Submissions: 9.7M
# Testcase Example:  '"babad"'
#
# Given a string s, return the longest palindromic substring in s.
# 
# 
# Example 1:
# 
# 
# Input: s = "babad"
# Output: "bab"
# Explanation: "aba" is also a valid answer.
# 
# 
# Example 2:
# 
# 
# Input: s = "cbbd"
# Output: "bb"
# 
# 
# 
# Constraints:
# 
# 
# 1 <= s.length <= 1000
# s consist of only digits and English letters.
# 
# 
#

# @lc code=start
class Solution:
    def longestPalindrome(self, s: str) -> str:

        if len(s) <=1:
            return s

        def expand_from_center(left, right):
            current_max = s[0]
            while True:
                while left >= 0 and right < len(s) and s[left] == s[right]:
                    left -= 1
                    right += 1

                current_max = s[left + 1: right]
                
                trial_left = left
                trial_right = right
                while trial_right < len(s) :
                    trial_left += 1
                    trial_right += 1

                    if trial_right == right:
                        continue
                    trial_right < len(s) 
                    if trial_right >= len(s) or s[trial_left] == s[trial_right] and s[trial_left:trial_right+1] == s[trial_left:trial_right+1][::-1]:
                        break


                if trial_left >= 0 and trial_right < len(s) and s[trial_left] == s[trial_right]:
                    left = trial_left
                    right = trial_right
                    current_max = s[left: right +1]
                else:
                    break
            return current_max
    
        odd = expand_from_center(0, 0)
        even = expand_from_center(0, 1)

        if len(odd) > len(even):
            return odd
        else:
            return even

# O(n)
        
# @lc code=end

Solution().longestPalindrome("aacabdkacaa")