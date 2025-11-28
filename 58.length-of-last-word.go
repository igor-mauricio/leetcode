package main

/*
 * @lc app=leetcode id=58 lang=golang
 *
 * [58] Length of Last Word
 */

// @lc code=start
func lengthOfLastWord(s string) int {
	iter := len(s) - 1
	characterCount := 0
	for iter >= 0 && s[iter] == ' ' {
		iter--
	}
	for iter >= 0 && s[iter] != ' ' {
		iter--
		characterCount++
	}
	return characterCount
}

// @lc code=end
