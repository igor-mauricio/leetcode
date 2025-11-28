package main

/*
 * @lc app=leetcode id=14 lang=golang
 *
 * [14] Longest Common Prefix
 */

// @lc code=start
func longestCommonPrefix(strs []string) string {
	output := ""
	for i := range 200 {
		for j := range strs {
			if len(strs[j]) <= i || strs[j][i] != strs[0][i] {
				return output
			}
		}
		output = strs[0][0 : i+1]
	}
	return output

}

// @lc code=end
