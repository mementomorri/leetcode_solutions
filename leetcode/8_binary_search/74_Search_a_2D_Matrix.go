package main

import "fmt"

func searchMatrix(matrix [][]int, target int) bool {
	fisrsts := make([]int, len(matrix))

	for i, row := range matrix {
		fisrsts[i] = row[0]
	}
	fmt.Println(fisrsts)
	targetRow := binarySearch(fisrsts, target, true)
	fmt.Println("Looking for the target")
	fmt.Println(matrix[targetRow])
	return binarySearch(matrix[targetRow], target, false) >= 0
}

func binarySearch(nums []int, target int, returnLast bool) int {
	l, r := 0, len(nums)-1
	var mid int

	for l <= r {
		mid = l + (r-l)/2
		fmt.Printf("l: %d, r: %d, mid: %d\n", l, r, mid)
		fmt.Printf("nums[l]: %d, nums[r]: %d, nums[mid]: %d\n", nums[l], nums[r], nums[mid])

		if nums[mid] < target {
			l = mid + 1
		} else if nums[mid] > target {
			r = mid - 1
		} else {
			return mid
		}
	}

	if returnLast {
		if nums[mid] > target && mid > 0 {
			mid--
		}
		fmt.Println("mid: ", mid)
		return mid
	} else {
		fmt.Println("mid: ", mid)
		return -1
	}
}

func main() {
	searchMatrix([][]int{{1, 3, 5, 7}, {10, 11, 16, 20}, {23, 30, 34, 50}}, 11)
}
