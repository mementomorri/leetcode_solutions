package main

import "fmt"

func combinationSum(candidates []int, target int) [][]int {
	result := make([][]int, 0)
	current := make([]int, 0)
	findCombinations(0, target, candidates, current, &result)
	return result
}

func findCombinations(index, target int, candidates []int, current []int, result *[][]int) {
	if target == 0 {
		combination := make([]int, len(current))
		copy(combination, current)
		*result = append(*result, combination)
		return
	}

	for i := index; i < len(candidates); i++ {
		if candidates[i] <= target {
			current = append(current, candidates[i])
			findCombinations(i, target-candidates[i], candidates, current, result)
			current = current[:len(current)-1]
		}
	}
}

func main() {
	testCase1 := []int{2, 3, 6, 7}
	testCase2 := []int{2, 3, 5}
	testCase3 := []int{2}

	fmt.Println(combinationSum(testCase1, 7))
	fmt.Println(combinationSum(testCase2, 9))
	fmt.Println(combinationSum(testCase3, 1))
}
