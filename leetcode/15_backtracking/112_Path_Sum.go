type TreeNode struct {
	Val   int
	Left  *TreeNode
	Right *TreeNode
}

func hasPathSum(root *TreeNode, targetSum int) bool {
	if root == nil {
		return false
	}

	return hasPathSumHelper(root, targetSum, 0)
}

func hasPathSumHelper(root *TreeNode, targetSum, currentSum int) bool {
	if root == nil {
		return false
	}
	currentSum += root.Val
	if root.Left == nil && root.Right == nil {
		return currentSum == targetSum
	}
	return hasPathSumHelper(root.Left, targetSum, currentSum) || hasPathSumHelper(root.Right, targetSum, currentSum)
}
