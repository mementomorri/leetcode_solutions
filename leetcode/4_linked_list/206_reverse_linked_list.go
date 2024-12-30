/**
 * Definition for singly-linked list.
 * type ListNode struct {
 *     Val int
 *     Next *ListNode
 * }
 */

package main

import "fmt"

type ListNode struct {
	Val  int
	Next *ListNode
}

func reverseList(head *ListNode) *ListNode {
	if head == nil {
		return head
	}

	cur := head
	next := head.Next
	cur.Next = nil
	var prev *ListNode

	for next != nil {
		prev = cur
		cur = next
		next = next.Next

		cur.Next = prev
	}
	return cur
}

func main() {
	test := &ListNode{
		Val: 1,
		Next: &ListNode{
			Val:  2,
			Next: nil,
		},
	}
	fmt.Println("input: [1, 2], reverseList:", reverseList(test))
}
