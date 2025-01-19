package main

import "fmt"

func subsets(nums []int) [][]int {
	if nums == nil {
		return [][]int{}
	}

	result := [][]int{}
	backtrack(nums, &result, []int{}, 0)
	return result
}

func backtrack(nums []int, result *[][]int, path []int, start int) {
	subsetCopy := make([]int, len(path))
	copy(subsetCopy, path)
	*result = append(*result, subsetCopy)

	for i := start; i < len(nums); i++ {
		path = append(path, nums[i])
		backtrack(nums, result, path, i+1)
		path = path[:len(path)-1]
	}
}

func main() {
	testCase1 := []int{1, 2, 3}
	testCase2 := []int{1, 2}
	testCase3 := []int{0}

	fmt.Println(subsets(testCase1))
	fmt.Println(subsets(testCase2))
	fmt.Println(subsets(testCase3))
}
