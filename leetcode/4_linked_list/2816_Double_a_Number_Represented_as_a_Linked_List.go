/*
* You are given the head of a non-empty linked list representing a non-negative integer without leading zeroes.
* Return the head of the linked list after doubling it.
* Example 1:
* Input: head = [1,8,9]
* Output: [3,7,8]
* Explanation: The figure above corresponds to the given linked list which represents the number 189. Hence, the returned linked list represents the number 189 * 2 = 378.
* Example 2:
* Input: head = [9,9,9]
* Output: [1,9,9,8]
* Explanation: The figure above corresponds to the given linked list which represents the number 999. Hence, the returned linked list reprersents the number 999 * 2 = 1998. 
* Constraints:
* The number of nodes in the list is in the range [1, 104]
* 0 <= Node.val <= 9
* The input is generated such that the list represents a number that does not have leading zeros, except the number 0 itself.
*/


/**
 * Definition for singly-linked list.
 * type ListNode struct {
 *     Val int
 *     Next *ListNode
 * }
 */
func doubleIt(head *ListNode) *ListNode {

	ans:=head
	if head.Val>=5{
		head=&ListNode{Val: 1, Next: head}
		ans=head
		head=head.Next
	}

	for head!=nil && head.Next!=nil{

		if head.Next.Val<5{
			head.Val=(head.Val*2)%10
		}else{
			head.Val=(head.Val*2+1)%10
		}
		
		head=head.Next
	}

	head.Val=(head.Val*2)%10
	return ans
}
