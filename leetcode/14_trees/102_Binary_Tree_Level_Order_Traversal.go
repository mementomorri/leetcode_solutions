type TreeNode struct {
	Val   int
	Left  *TreeNode
	Right *TreeNode
}

func levelOrder(root *TreeNode) [][]int {
	res := make([][]int, 0)

	queue := make([]*TreeNode, 0)
	if root != nil {
		queue = append(queue, root)
	}

	var cur *TreeNode
	level := 0
	for len(queue) > 0 {
		res = append(res, []int{})
		qLen := len(queue)
		for i := 0; i < qLen; i++ {
			cur = queue[0]
			queue = queue[1:]
			res[level] = append(res[level], cur.Val)
			if cur.Left != nil {
				queue = append(queue, cur.Left)
			}
			if cur.Right != nil {
				queue = append(queue, cur.Right)
			}
		}
		level++
	}
	return res
}
