import "slices"

func maximumWealth(accounts [][]int) int {
	value := 0
	round := make([]int, len(accounts))

	for i := 0; i < len(accounts); i++ {
		value = 0
		for j := 0; j < len(accounts[i]); j++ {
			value += accounts[i][j]
		}
		round[i] = value
	}
	ans := slices.Max(round)

	return ans
}
