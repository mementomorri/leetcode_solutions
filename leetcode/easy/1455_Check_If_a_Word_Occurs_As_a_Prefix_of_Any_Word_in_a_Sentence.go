import "strings"

func isPrefixOfWord(sentence string, searchWord string) int {
	sentence_list := strings.Split(sentence, " ")
	for i, w := range sentence_list {
		if strings.HasPrefix(w, searchWord) {
			return i + 1
		}
	}
	return -1
}
