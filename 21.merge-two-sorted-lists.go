package leetcode

/*
 * @lc app=leetcode id=21 lang=golang
 *
 * [21] Merge Two Sorted Lists
 */

type ListNode struct {
	Val  int
	Next *ListNode
}

// @lc code=start
/**
 * Definition for singly-linked list.
 * type ListNode struct {
 *     Val int
 *     Next *ListNode
 * }
 */
func mergeTwoLists(list1 *ListNode, list2 *ListNode) *ListNode {
	merged := &ListNode{}
	var mergedStart *ListNode

	appendFromList1 := func() {
		merged.Next = &ListNode{list1.Val, nil}
		merged = merged.Next
		list1 = list1.Next
	}
	appendFromList2 := func() {
		merged.Next = &ListNode{list2.Val, nil}
		merged = merged.Next
		list2 = list2.Next
	}
	if list1 == nil && list2 == nil {
		return nil
	} else if list2 == nil && list1 != nil {
		mergedStart = &ListNode{list1.Val, nil}
		list1 = list1.Next
	} else if list1 == nil && list2 != nil {
		mergedStart = &ListNode{list2.Val, nil}
		list2 = list2.Next
	} else if list1.Val <= list2.Val {
		mergedStart = &ListNode{list1.Val, nil}
		list1 = list1.Next
	} else {
		mergedStart = &ListNode{list2.Val, nil}
		list2 = list2.Next
	}
	merged = mergedStart
	for list1 != nil || list2 != nil {
		if list2 == nil && list1 != nil {
			appendFromList1()
			continue
		}
		if list1 == nil && list2 != nil {
			appendFromList2()
			continue
		}
		if list1.Val <= list2.Val {
			appendFromList1()
		} else {
			appendFromList2()
		}
	}
	return mergedStart
}

// @lc code=end
