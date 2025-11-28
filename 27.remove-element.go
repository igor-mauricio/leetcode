package main

/*
 * @lc app=leetcode id=27 lang=golang
 *
 * [27] Remove Element
 */

// @lc code=start

func removeElement(nums []int, val int) int {
	searchI := 0
	maxSearchI := len(nums) - 1
	writeI := 0
	for searchI <= maxSearchI {
		for searchI <= maxSearchI && nums[searchI] == val {
			searchI++
		}
		if searchI <= maxSearchI && nums[searchI] != val {
			nums[writeI] = nums[searchI]
			writeI++
		}
		searchI++
	}
	return writeI
}

// @lc code=end

// func main() {
// 	nums := []int{3, 2, 2, 3}
// 	val := 3

// 	result := removeElement(nums, val)
// 	print(result, nums)
// }
