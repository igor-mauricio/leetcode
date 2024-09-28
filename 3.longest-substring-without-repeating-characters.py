#
# @lc app=leetcode id=3 lang=python3
#
# [3] Longest Substring Without Repeating Characters
#
# https://leetcode.com/problems/longest-substring-without-repeating-characters/description/
#
# algorithms
# Medium (35.49%)
# Likes:    40274
# Dislikes: 1934
# Total Accepted:    6.4M
# Total Submissions: 17.9M
# Testcase Example:  '"abcabcbb"'
#
# Given a string s, find the length of the longest substring without repeating
# characters.
# 
# 
# Example 1:
# 
# 
# Input: s = "abcabcbb"
# Output: 3
# Explanation: The answer is "abc", with the length of 3.
# 
# 
# Example 2:
# 
# 
# Input: s = "bbbbb"
# Output: 1
# Explanation: The answer is "b", with the length of 1.
# 
# 
# Example 3:
# 
# 
# Input: s = "pwwkew"
# Output: 3
# Explanation: The answer is "wke", with the length of 3.
# Notice that the answer must be a substring, "pwke" is a subsequence and not a
# substring.
# 
# 
# 
# Constraints:
# 
# 
# 0 <= s.length <= 5 * 10^4
# s consists of English letters, digits, symbols and spaces.
# 
# 
#

# @lc code=start
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        hashmap = {}
        max_len = 0
        current_len = 0
        i = 0
        while i < len(s):
            current_char = s[i]
            if current_char in hashmap:
                i = hashmap[current_char] + 1
                hashmap = {}
                max_len = current_len if current_len > max_len else max_len
                current_char = s[i]
                current_len = 0
            hashmap[current_char] = i
            current_len += 1
            i += 1
        max_len = current_len if current_len > max_len else max_len
        return max_len
            
            
Solution().lengthOfLongestSubstring("dvdf")
            
        
# @lc code=end

