import "strings"

func addSpaces(s string, spaces []int) string {
	i, j := 0, 0
	res := make([]string, 0)

	for i < len(s) && j < len(spaces) {
		if i < spaces[j] {
			res = append(res, s[i:i+1])
			i++
		} else {
			res = append(res, " ")
			j++
		}
	}
	if i < len(s) {
		res = append(res, s[i:])
	}

	return strings.Join(res, "")
}
