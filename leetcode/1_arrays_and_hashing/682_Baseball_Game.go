import "strconv"

func calPoints(operations []string) int {
	result := make([]int, 0)
	var item int
	for _, op := range operations {
		switch op {
		case "C":
			result = result[0 : len(result)-1]
		case "D":
			result = append(result, result[len(result)-1]*2)
		case "+":
			result = append(result, result[len(result)-1]+result[len(result)-2])
		default:
			item, _ = strconv.Atoi(op)
			result = append(result, item)
		}
	}
	sum := 0
	for _, valueInt := range result {
		sum += valueInt
	}
	return sum
}
