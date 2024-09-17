package main

import (
	"strings"
)

func uncommonFromSentences(sentence1 string, sentence2 string) []string {
	wordCount := make(map[string]int)
	words := strings.Fields(sentence1 + " " + sentence2)

	// Count the occurrences of each word
	for _, word := range words {
		wordCount[word]++
	}

	// Collect the uncommon words
	var uncommonWords []string
	for word, count := range wordCount {
		if count == 1 {
			uncommonWords = append(uncommonWords, word)
		}
	}

	return uncommonWords
}
