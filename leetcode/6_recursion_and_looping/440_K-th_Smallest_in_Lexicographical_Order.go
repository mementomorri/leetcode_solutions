func findKthNumber(n int, k int) int {
	curr := 1
	k -= 1
	for k > 0 {
		count := count(curr, curr+1, n)
		if count <= k {
			curr += 1
			k -= count
		} else {
			curr *= 10
			k--
		}
	}

	return curr
}

func count(curr, next int, n int) int {
	count := 0
	for curr <= n {
		count += next - curr
		curr *= 10
		next *= 10

		next = min(next, n+1)
	}

	return count
}
