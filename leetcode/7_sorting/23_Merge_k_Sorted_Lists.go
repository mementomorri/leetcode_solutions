/**
 * Definition for singly-linked list.
 * type ListNode struct {
 *     Val int
 *     Next *ListNode
 * }
 */
func mergeKLists(lists []*ListNode) *ListNode {
	if len(lists) == 0 {
		return nil
	}

	return mergeSort(lists, 0, len(lists)-1)
}

func mergeSort(nums []*ListNode, s, e int) *ListNode {
	if s == e {
		return nums[s]
	}

	m := s + (e-s)/2
	left := mergeSort(nums, s, m)
	right := mergeSort(nums, m+1, e)

	return merge(left, right)
}

func merge(left, right *ListNode) *ListNode {
	tail := &ListNode{Val: -1}
	head := tail

	for left != nil && right != nil {
		if left.Val < right.Val {
			head.Next = left
			left = left.Next
		} else {
			head.Next = right
			right = right.Next
		}
		head = head.Next
	}

	if left != nil {
		head.Next = left
	}
	if right != nil {
		head.Next = right
	}
	return tail.Next
}

