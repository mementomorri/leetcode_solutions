func numSubarrayProductLessThanK(nums []int, k int) int {
	if k <= 1 {
		return 0
	}
	var ans, left int
	curr := 1
	for right := 0; right < len(nums); right++ {
		curr *= nums[right]
		for curr >= k {
			curr /= nums[left]
			left++
		}
		ans += right - left + 1
	}
	return ans
}
