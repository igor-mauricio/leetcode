package main

/*
 * @lc app=leetcode id=20 lang=golang
 *
 * [20] Valid Parentheses
 */

// @lc code=start

func isValid(s string) bool {
	stack := []byte{}
	for i := range s {
		if len(stack) <= 0 {
			stack = append(stack, s[i])
			continue
		}
		switch s[i] {
		case ']':
			if stack[len(stack)-1] == '[' {
				stack = stack[:len(stack)-1]
				continue
			}
		case ')':
			if stack[len(stack)-1] == '(' {
				stack = stack[:len(stack)-1]
				continue
			}
		case '}':
			if stack[len(stack)-1] == '{' {
				stack = stack[:len(stack)-1]
				continue
			}
		}
		stack = append(stack, s[i])
	}
	return len(stack) == 0
}

// @lc code=end
