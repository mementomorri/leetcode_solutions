package main

import (
	"fmt"
)

// List represents a slice-based list that holds values of any type.
type List[T comparable] struct {
	elements []T
}

// Add adds a new element to the end of the list.
func (l *List[T]) Add(value T) {
	l.elements = append(l.elements, value)
}

// Remove removes the first occurrence of a value from the list.
func (l *List[T]) Remove(value T) {
	for i, v := range l.elements {
		if v == value {
			l.elements = append(l.elements[:i], l.elements[i+1:]...) // Remove the element
			return
		}
	}
}

// Search checks if a value exists in the list.
func (l *List[T]) Search(value T) bool {
	for _, v := range l.elements {
		if v == value {
			return true
		}
	}
	return false
}

// Display prints the elements of the list.
func (l *List[T]) Display() {
	for _, v := range l.elements {
		fmt.Print(v, " ")
	}
	fmt.Println()
}

func main() {
	list := &List[int]{} // Create a list for integers

	// Adding elements to the list
	list.Add(10)
	list.Add(20)
	list.Add(30)
	fmt.Print("List after adding elements: ")
	list.Display() // Output: 10 20 30

	// Searching for an element
	fmt.Println("Searching for 20:", list.Search(20)) // Output: true
	fmt.Println("Searching for 40:", list.Search(40)) // Output: false

	// Removing an element
	list.Remove(20)
	fmt.Print("List after removing 20: ")
	list.Display() // Output: 10 30

	// Removing a non-existent element
	list.Remove(40)
	fmt.Print("List after trying to remove 40: ")
	list.Display() // Output: 10 30
}
