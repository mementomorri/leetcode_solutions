package main

import "fmt"

func countStudents(students []int, sandwiches []int) int {
	students_amount := make(map[int]int)
	for _, student := range students {
		students_amount[student]++
	}

	fmt.Println(students_amount)
	for _, sandwich := range sandwiches {
		if students_amount[sandwich] <= 0 {
			break
		}
		students_amount[sandwich]--
	}

	fmt.Println(students_amount)
	return students_amount[0] + students_amount[1]
}

func main() {
	students1 := []int{1, 1, 0, 0}
	sandwiches1 := []int{0, 1, 0, 1}
	fmt.Println("Running test case 1: students = [1,1,0,0], sandwiches = [0,1,0,1]")
	fmt.Println(countStudents(students1, sandwiches1))
	students2 := []int{1, 1, 1, 0, 0, 1}
	sandwiches2 := []int{1, 0, 0, 0, 1, 1}
	fmt.Println("Running test case 2: students = [1,1,1,0,0,1], sandwiches = [1,0,0,0,1,1]")
	fmt.Println(countStudents(students2, sandwiches2))
}
