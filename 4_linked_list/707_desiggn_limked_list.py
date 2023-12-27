"""
Design your implementation of the linked list. You can choose to use a singly or doubly linked list.
A node in a singly linked list should have two attributes: val and next. val is the value of the current node, and next is a pointer/reference to the next node.
If you want to use the doubly linked list, you will need one more attribute prev to indicate the previous node in the linked list. Assume all nodes in the linked list are 0-indexed.

Implement the MyLinkedList class:

    MyLinkedList() Initializes the MyLinkedList object.
    int get(int index) Get the value of the indexth node in the linked list. If the index is invalid, return -1.
    void addAtHead(int val) Add a node of value val before the first element of the linked list. After the insertion, the new node will be the first node of the linked list.
    void addAtTail(int val) Append a node of value val as the last element of the linked list.
    void addAtIndex(int index, int val) Add a node of value val before the indexth node in the linked list. If index equals the length of the linked list, the node will be appended to the end of the linked list. If index is greater than the length, the node will not be inserted.
    void deleteAtIndex(int index) Delete the indexth node in the linked list, if the index is valid.



Example 1:

Input
["MyLinkedList", "addAtHead", "addAtTail", "addAtIndex", "get", "deleteAtIndex", "get"]
[[], [1], [3], [1, 2], [1], [1], [1]]
Output
[null, null, null, null, 2, null, 3]

Explanation
MyLinkedList myLinkedList = new MyLinkedList();
myLinkedList.addAtHead(1);
myLinkedList.addAtTail(3);
myLinkedList.addAtIndex(1, 2);    // linked list becomes 1->2->3
myLinkedList.get(1);              // return 2
myLinkedList.deleteAtIndex(1);    // now the linked list is 1->3
myLinkedList.get(1);              // return 3



Constraints:

    0 <= index, val <= 1000
    Please do not use the built-in LinkedList library.
    At most 2000 calls will be made to get, addAtHead, addAtTail, addAtIndex and deleteAtIndex.
"""

class ListNode:
    def __init__(self, val=None, next=None):
        self.val = val
        self.next = next

    def __str__(self):
        return str(self.val)


class MyLinkedList:
    def __init__(self):
        self.head = ListNode()
        self.tail = self.head

    def get(self, index: int) -> int:
        i = 0
        current_node = self.head
        while i < index and current_node:
            current_node = current_node.next
            i += 1
        if current_node and current_node.val is not None:
            return current_node.val
        return -1

    def addAtHead(self, val: int) -> None:
        if self.head.val is not None:
            self.head = ListNode(val, self.head)
        else:
            self.head = ListNode(val)
            self.tail = self.head

    def addAtTail(self, val: int) -> None:
        if self.tail.val is not None:
            self.tail.next = ListNode(val)
            self.tail = self.tail.next
        else:
            self.tail = ListNode(val)
            self.head = self.tail

    def addAtIndex(self, index: int, val: int) -> None:
        if index == 0:
            if self.head.val is None:
                self.head = ListNode(val)
            else:
                self.head = ListNode(val, self.head)
            return None
        i = 0
        current_node = self.head
        while i < index - 1 and current_node:
            current_node = current_node.next
            i += 1
        if current_node:
            current_node.next = ListNode(val, current_node.next)
            if self.tail == current_node:
                self.tail = current_node.next
        if i+1 == index and current_node and not current_node.next:
            self.tail.next = ListNode(val)
            self.tail = self.tail.next
        return None

    def deleteAtIndex(self, index: int) -> None:
        if index == 0:
            self.head = self.head.next
            return None
        i=0
        current_node = self.head
        while i < index - 1 and current_node:
            current_node = current_node.next
            i += 1
        if current_node and current_node.next:
            if self.tail == current_node.next:
                self.tail = current_node
            current_node.next = current_node.next.next

    def __str__(self):
        curr = self.head
        res = ''
        while curr:
            res += str(curr)+ ' -> '
            curr = curr.next
        return res


# Your MyLinkedList object will be instantiated and called as such:
if __name__ == '__main__':
    myLinkedList = MyLinkedList()
    # myLinkedList.addAtHead(7)
    # myLinkedList.addAtHead(2)
    # myLinkedList.addAtHead(1)
    # myLinkedList.addAtIndex(3, 0)
    # print(myLinkedList)
    # print('tail=',myLinkedList.tail)
    # myLinkedList.deleteAtIndex(2)
    # print(myLinkedList)
    # myLinkedList.addAtHead(6)
    # print(myLinkedList)
    # myLinkedList.addAtTail(4)
    # print(myLinkedList)
    # print(myLinkedList.get(4))
    #
    myLinkedList.addAtIndex(0, 10)
    myLinkedList.addAtIndex(0, 20)
    myLinkedList.addAtIndex(1, 30)
    print(myLinkedList.get(0))
    print(myLinkedList)