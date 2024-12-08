import "math"

func sortedSquares(nums []int) []int {
	left, right := 0, len(nums)-1
	res := make([]int, len(nums))
	var sq int
	for i := len(nums) - 1; i >= 0; i-- {
		if math.Abs(float64(nums[left])) < math.Abs(float64(nums[right])) {
			sq = nums[right]
			right--
		} else {
			sq = nums[left]
			left++
		}
		res[i] = sq * sq
	}
	return res
}
