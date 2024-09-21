package main

var (
	stack  [1e5]int
	result = make([]int, 5e4+1)
)

func lexicalOrder(n int) []int {
	stackSize := 0
	resultSize := 0

	stack[stackSize] = 0
	stackSize++

	for stackSize > 0 {
		last := stack[stackSize-1]
		stackSize--

		result[resultSize] = last
		resultSize++

		for i := 9; i >= 0; i-- {
			next := last*10 + i

			if next > n || next == 0 {
				continue
			}

			stack[stackSize] = next
			stackSize++
		}
	}

	return result[1:resultSize]
}
