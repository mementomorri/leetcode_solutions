type TreeNode struct {
	Val   int
	Left  *TreeNode
	Right *TreeNode
}

func kthSmallest(root *TreeNode, k int) int {
	return inorderTraversal(root)[k-1]
}

func inorderTraversal(root *TreeNode) []int {
	var data []int

	var helper func(*TreeNode, *[]int)

	helper = func(root *TreeNode, data *[]int) {
		if root == nil {
			return
		}
		helper(root.Left, data)
		*data = append(*data, root.Val)
		helper(root.Right, data)
	}

	helper(root, &data)
	return data
}
