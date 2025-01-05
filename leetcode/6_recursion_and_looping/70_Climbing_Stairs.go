func climbStairs(n int) int {
	mem := map[int]int{1: 1, 2: 2, 3: 3}
	for i := 4; i <= n; i++ {
		mem[i] = mem[i-1] + mem[i-2]
	}
	return mem[n]
}
