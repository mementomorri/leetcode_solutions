func sortArray(nums []int) []int {
	for i := 1; i < len(nums); i++ {
		for j := i - 1; j >= 0 && nums[j] > nums[j+1]; j-- {
			nums[j+1], nums[j] = nums[j], nums[j+1]
		}
	}
	return nums
}
