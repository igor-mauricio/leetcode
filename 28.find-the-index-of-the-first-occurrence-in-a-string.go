package main

/*
 * @lc app=leetcode id=28 lang=golang
 *
 * [28] Find the Index of the First Occurrence in a String
 */

// @lc code=start
func strStr(haystack string, needle string) int {
	needleIMax := len(needle) - 1
	haystackIMax := len(haystack) - 1
	for haystackI := 0; haystackI <= haystackIMax; haystackI++ {
		found := true
		for needleI := 0; needleI <= needleIMax; needleI++ {
			if haystackI+needleI > haystackIMax {
				found = false
				break
			}
			if haystack[haystackI+needleI] != needle[needleI] {
				found = false
				break
			}
		}
		if found {
			return haystackI
		}
	}
	return -1
}

// @lc code=end

func main() {
	print(strStr("sadbutsad", "sad"))
}
