package main

import "fmt"

type Node struct {
	Val  int
	Next *Node
}

type MyLinkedList struct {
	Head *Node
	Size int
}

func Constructor() MyLinkedList {
	return MyLinkedList{&Node{}, 0}
}

func (this *MyLinkedList) Get(index int) int {
	if index < 0 || index >= this.Size {
		return -1
	}
	curr := this.Head
	for i := 0; i <= index; i++ {
		curr = curr.Next
	}
	return curr.Val
}

func (this *MyLinkedList) AddAtHead(val int) {
	node := &Node{val, this.Head.Next}
	this.Head.Next = node
	this.Size++
}

func (this *MyLinkedList) AddAtTail(val int) {
	node := &Node{val, nil}
	curr := this.Head
	for curr.Next != nil {
		curr = curr.Next
	}
	curr.Next = node
	this.Size++
}

func (this *MyLinkedList) AddAtIndex(index int, val int) {
	if index < 0 || index > this.Size {
		return
	}
	node := &Node{val, nil}
	curr := this.Head
	for i := 0; i < index; i++ {
		curr = curr.Next
	}
	node.Next = curr.Next
	curr.Next = node
	this.Size++
}

func (this *MyLinkedList) DeleteAtIndex(index int) {
	if index < 0 || index >= this.Size {
		return
	}
	curr := this.Head
	for i := 0; i < index; i++ {
		curr = curr.Next
	}
	curr.Next = curr.Next.Next
	this.Size--
}

func (this *MyLinkedList) ShowAll() {
	count := 0
	for cur := this.Head; cur != nil; cur = cur.Next {
		fmt.Printf("%d -> %d\n", count, cur.Val)
		count++
	}
}

/**
 * Your MyLinkedList object will be instantiated and called as such:
 * obj := Constructor();
 * param_1 := obj.Get(index);
 * obj.AddAtHead(val);
 * obj.AddAtTail(val);
 * obj.AddAtIndex(index,val);
 * obj.DeleteAtIndex(index);
 */

func main() {
	MyLinkedList := MyLinkedList{}
	MyLinkedList.AddAtHead(1)
	MyLinkedList.AddAtTail(3)
	MyLinkedList.AddAtIndex(1, 2)
	MyLinkedList.ShowAll()
	MyLinkedList.Get(1)
	MyLinkedList.DeleteAtIndex(1)
	MyLinkedList.Get(1)
	MyLinkedList.ShowAll()
}
