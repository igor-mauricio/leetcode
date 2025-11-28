package main

/*
 * @lc app=leetcode id=26 lang=golang
 *
 * [26] Remove Duplicates from Sorted Array
 */

// @lc code=start
func removeDuplicates(nums []int) int {
	index := 0
	for i := range nums {
		if nums[i] == nums[index] {
			continue
		}
		index++
		nums[index] = nums[i]
	}
	return index + 1
}

// @lc code=end
