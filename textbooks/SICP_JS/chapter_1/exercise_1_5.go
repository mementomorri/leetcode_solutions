package main

import "fmt"

type Callable func()

func p() Callable { return p() }

func test(x int, y Callable) Callable {
	if x != 0 {
		fmt.Println("Infinite loop")
		return y
	}
	fmt.Println("Infinite loop")
	return y
}

func main() {
	fmt.Println(test(9, p()))
}
