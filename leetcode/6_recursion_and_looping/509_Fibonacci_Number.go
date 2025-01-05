package main

import "fmt"

func fib(n int) int {
	mem := map[int]int{0: 0, 1: 1}
	for i := 2; i <= n; i++ {
		mem[i] = mem[i-1] + mem[i-2]
	}
	return mem[n]
}

func main() {
	fmt.Println(fib(5))
	fmt.Println(fib(1))
	fmt.Println(fib(10))
}
