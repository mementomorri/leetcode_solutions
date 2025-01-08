type TreeNode struct {
	Val   int
	Left  *TreeNode
	Right *TreeNode
}

func lowestCommonAncestor(root, p, q *TreeNode) *TreeNode {
	if root == nil {
		return nil
	}

	var (
		l int
		r int
	)

	if p.Val > q.Val {
		l = q.Val
		r = p.Val
	} else {
		l = p.Val
		r = q.Val
	}

	if root.Val >= l && root.Val <= r {
		return root
	} else if root.Val < l {
		return lowestCommonAncestor(root.Right, p, q)
	} else {
		return lowestCommonAncestor(root.Left, p, q)
	}
}
