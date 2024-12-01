package main

import (
	"encoding/csv"
	"fmt"
	"log"
	"math"
	"os"
	"sort"
	"strconv"
)

func find_total_distance(data [][]string) int {
	res := 0.0
	left := make([]int, 0)
	right := make([]int, 0)
	l := 0
	r := 0
	for _, line := range data {

		l, _ = strconv.Atoi(line[0])
		r, _ = strconv.Atoi(line[1])
		left = append(left, l)
		right = append(right, r)
	}
	sort.Ints(left)
	sort.Ints(right)

	for i := 0; i < len(left); i++ {
		l = left[i]
		r = right[i]
		res += math.Abs(float64(l - r))
	}

	return int(res)
}

func main() {
	// open file
	f, err := os.Open("day1/input.csv")
	if err != nil {
		log.Fatal(err)
	}

	// remember to close the file at the end of the program
	defer f.Close()

	// read csv values using csv.Reader
	csvReader := csv.NewReader(f)
	if _, err := csvReader.Read(); err != nil {
		panic(err)
	}
	data, err := csvReader.ReadAll()
	if err != nil {
		log.Fatal(err)
	}

	// convert records to array of structs
	res := find_total_distance(data)

	// print the array
	fmt.Printf("%+v\n", res)
}
