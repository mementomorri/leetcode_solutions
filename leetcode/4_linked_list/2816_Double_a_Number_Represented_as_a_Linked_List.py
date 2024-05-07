"""
You are given the head of a non-empty linked list representing a non-negative integer without leading zeroes.

Return the head of the linked list after doubling it.

 

Example 1:


Input: head = [1,8,9]
Output: [3,7,8]
Explanation: The figure above corresponds to the given linked list which represents the number 189. Hence, the returned linked list represents the number 189 * 2 = 378.
Example 2:


Input: head = [9,9,9]
Output: [1,9,9,8]
Explanation: The figure above corresponds to the given linked list which represents the number 999. Hence, the returned linked list reprersents the number 999 * 2 = 1998. 
 

Constraints:

The number of nodes in the list is in the range [1, 104]
0 <= Node.val <= 9
The input is generated such that the list represents a number that does not have leading zeros, except the number 0 itself.
"""


def doubleIt(head: ListNode) -> ListNode:
    nums = []
    val = 0
    while head:
        nums.append(head.val)
        head = head.next
    tail = None
    while nums or val != 0:
        tail = ListNode(0, tail)

        if nums:
            val += nums.pop() * 2
        tail.val = val % 10
        val //= 10

    return tail


if __name__ == "__main__":
    test1 = ListNode(1, ListNode(8, ListNode(9)))
    test2 = ListNode(9, ListNode(9, ListNode(9)))

    print(doubleIt(test1), "== [3,7,8]")
    print(doubleIt(test2), "== [1,9,9,8]")
