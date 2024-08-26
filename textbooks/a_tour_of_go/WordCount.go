package main

import (
	"golang.org/x/tour/wc"
	"strings"
)

func WordCount(s string) (res map[string]int) {
	split := strings.Fields(s)
	res = make(map[string]int)
	for i := range split {
		word := split[i]
		_, ok := res[word]
		if ok {
			res[word] += 1
		} else {
			res[word] = 1
		}
	}
	return res
}

func main() {
	wc.Test(WordCount)
}
