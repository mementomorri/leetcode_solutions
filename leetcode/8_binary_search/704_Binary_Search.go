func search(nums []int, target int) int {
	l, r := 0, len(nums)-1

	for l <= r {
		mid := l + (r-l)/2
		if nums[mid] > target {
			r = mid - 1
		} else if nums[mid] < target {
			l = mid + 1
		} else {
			return mid
		}
	}
	return -1
}

// func searchB(nums []int, target int) int {
// 	idx := sort.SearchInts(nums, target)
// 	if idx >= len(nums) || nums[idx] != target {
// 		return -1
// 	}
// 	return idx
// }
