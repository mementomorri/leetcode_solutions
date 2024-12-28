package main

import "fmt"

func isValid(s string) bool {
	matches := map[string]string{
		"(": ")",
		"[": "]",
		"{": "}",
	}
	bracketStack := []string{}

	for _, c := range s {
		fmt.Println(string(c), bracketStack)
		if len(bracketStack) > 0 && string(c) == matches[bracketStack[len(bracketStack)-1]] {
			bracketStack = bracketStack[:len(bracketStack)-1]
			fmt.Println("pop from bracketStack")
		} else {
			bracketStack = append(bracketStack, string(c))
			fmt.Println("append to bracketStack")
		}
	}
	fmt.Println(bracketStack)
	return len(bracketStack) == 0
}

func main() {
	s := "()[]{}"
	fmt.Println(isValid(s))
}
