package main

/*
 * @lc app=leetcode id=36 lang=golang
 *
 * [36] Valid Sudoku
 */

// @lc code=start
func isValidSudoku(board [][]byte) bool {
	numbersVertical := make([][]bool, 9)
	numbersHorizontal := make([][]bool, 9)
	numbersBoxes := make([][]bool, 9)
	for i := range 9 {
		numbersHorizontal[i] = make([]bool, 9)
		numbersVertical[i] = make([]bool, 9)
		numbersBoxes[i] = make([]bool, 9)
	}
	for i := range 9 {
		for j := range 9 {
			number := board[i][j] - '1'
			//Empty spaces
			if number < 0 || number > 8 {
				continue
			}
			//Vertical Count
			if numbersVertical[i][number] {
				return false
			}
			numbersVertical[i][number] = true
			//Horizontal Count
			if numbersHorizontal[j][number] {
				return false
			}
			numbersHorizontal[j][number] = true
			//Boxes count
			box := (i - i%3) + j/3
			if numbersBoxes[box][number] {
				return false
			}
			numbersBoxes[box][number] = true
		}
	}
	return true
}

// @lc code=end
