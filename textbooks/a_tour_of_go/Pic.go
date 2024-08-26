package main

import "golang.org/x/tour/pic"

func Pic(dx, dy int) [][]uint8 {
	var res = make([][]uint8, dy)
	for i:= range dy{
		res[i] = make([]uint8, dx)
		for l := range dx{
			res[i][l] = uint8(i^l)
		}
	}
	return res
}

func main() {
	pic.Show(Pic)
}
