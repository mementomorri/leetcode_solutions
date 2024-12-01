import "slices"

func checkIfExist(arr []int) bool {
	for i := 0; i < len(arr); i++ {
		if slices.Contains(arr[0:i], 2*arr[i]) || slices.Contains(arr[i+1:], 2*arr[i]) {
			return true
		}
	}
	return false
}
