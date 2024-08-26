/**
 * Definition for a Node.
 * type Node struct {
 *     Val int
 *     Children []*Node
 * }
 */

func helper(node *Node, res *[]int) {
	if node == nil {
		return
	}
	if len(node.Children) > 0 {
		for _, i := range node.Children {
			helper(i, res)
		}
	}
	*res = append(*res, node.Val)
}

func postorder(root *Node) []int {
	res := []int{}
	helper(root, &res)
	return res
}
