func longestOnes(nums []int, k int) int {
	var left, ans, cur int
	for right := 0; right < len(nums); right++ {
		if nums[right] == 0 {
			curr++
		}
		if curr > k {
			if nums[left] == 0 {
				curr--
			}
			left++
		}
		ans = max(ans, right-left+1)
	}
	return ans
}
