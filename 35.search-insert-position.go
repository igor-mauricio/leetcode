/*
 * @lc app=leetcode id=35 lang=golang
 *
 * [35] Search Insert Position
 */
package main

// @lc code=start
func searchInsert(nums []int, target int) int {
	minIndex := 0
	maxIndex := len(nums) - 1
	newIndex := func(min, max int) int {
		return (int)((min + max) / 2)
	}
	searchI := newIndex(minIndex, maxIndex)
	for {
		if target == nums[searchI] {
			return searchI
		}
		if target <= nums[minIndex] {
			return minIndex
		}
		if target == nums[maxIndex] {
			return maxIndex
		}
		if target > nums[maxIndex] {
			return maxIndex + 1
		}
		if maxIndex == minIndex+1 {
			return maxIndex
		}
		if nums[searchI] < target {
			minIndex = searchI
			searchI = newIndex(minIndex, maxIndex)
			continue
		}
		if nums[searchI] > target {
			maxIndex = searchI
			searchI = newIndex(minIndex, maxIndex)
			continue
		}
	}
}

// @lc code=end
