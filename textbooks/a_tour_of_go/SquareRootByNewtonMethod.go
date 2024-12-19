package main

import (
	"fmt"
	"math"
)

func Sqrt(x float64) float64 {
	z := x
	var prevZ float64
	for {
		prevZ = z
		z -= (z*z - x) / (2 * z)
		if math.Abs(z-prevZ) < 1e-10 {
			break
		}
	}
	return z
}

func main() {
	for _, x := range []float64{1, 2, 3, 4, 9, 16, 25} {
		fmt.Printf("Approximate square root of %f: %f\n", x, Sqrt(x))
		fmt.Printf("Actual square root of %f: %f\n", x, math.Sqrt(x))
		fmt.Println()
	}
}
