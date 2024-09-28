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
        largest = ""
    
        for i in range(len(s)):
            for j in range(i + len(largest), len(s)):
                s_slice = s[i:j+1]
                if self.isPalindrome(s_slice) and len(s_slice) > len(largest):
                    largest = s_slice

        return largest

    def isPalindrome(self, text: str) -> bool:
        for i in range(len(text)//2):
            if text[i] != text[len(text)-1 -i]:
                return False
        return True





        


        
# @lc code=end

