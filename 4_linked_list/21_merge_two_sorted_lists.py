"""
You are given the heads of two sorted linked lists list1 and list2.

Merge the two lists into one sorted list. The list should be made by splicing together the nodes of the first two lists.

Return the head of the merged linked list.



Example 1:

Input: list1 = [1,2,4], list2 = [1,3,4]
Output: [1,1,2,3,4,4]

Example 2:

Input: list1 = [], list2 = []
Output: []

Example 3:

Input: list1 = [], list2 = [0]
Output: [0]



Constraints:

    The number of nodes in both lists is in the range [0, 50].
    -100 <= Node.val <= 100
    Both list1 and list2 are sorted in non-decreasing order.
"""
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def mergeTwoLists(list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
    if list1 and list2:
        if list1.val <= list2.val:
            res = ListNode(list1.val)
            item1 = list1.next
            item2 = list2
        else:
            res = ListNode(list2.val)
            item1 = list1
            item2 = list2.next
    else:
        if list1:
            res = ListNode(list1.val)
            item1 = list1.next
            item2 = None
        elif list2:
            res = ListNode(list2.val)
            item2 = list2.next
            item1 = None
        else:
            return None
    cur_node = res

    while item1 and item2:
        print(item1.val, item2.val)
        if item1.val <= item2.val:
            cur_node.next = item1
            item1 = item1.next
        else:
            cur_node.next = item2
            item2 = item2.next
        cur_node = cur_node.next
    if item1:
        cur_node.next = item1
    if item2:
        cur_node.next = item2
    return res