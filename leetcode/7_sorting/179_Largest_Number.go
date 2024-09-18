import (
	"sort"
	"strconv"
	"strings"
)

func largestNumber(nums []int) string {
	numStrs := make([]string, len(nums))

	// Convert integers to strings
	for i, num := range nums {
		numStrs[i] = strconv.Itoa(num)
	}

	// Sort based on custom rules
	sort.Slice(numStrs, func(i, j int) bool {
		return numStrs[i]+numStrs[j] > numStrs[j]+numStrs[i]
	})

	// If the largest number is "0", return "0"
	if numStrs[0] == "0" {
		return "0"
	}

	// Join the sorted strings to form the largest number
	return strings.Join(numStrs, "")
}
