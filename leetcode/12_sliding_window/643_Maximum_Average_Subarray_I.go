func findMaxAverage(nums []int, k int) float64 {
	sum := 0
	for _, num := range nums[:k] {
		sum += num
	}
	max_sum := sum
	for i := k; i < len(nums); i++ {
		sum -= nums[i-k]
		sum += nums[i]
		max_sum = max(sum, max_sum)
	}
	return float64(max_sum) / float64(k)
}
