# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if not root:
            return False
        return self.hasPathSumHelper(root, targetSum, 0)

    def hasPathSumHelper(self, root: TreeNode, targetSum: int, currentSum: int) -> bool:
        if not root:
            return False
        currentSum += root.val
        if not root.left and not root.right:
            return currentSum == targetSum
        return self.hasPathSumHelper(root.left, targetSum, currentSum) or self.hasPathSumHelper(
            root.right, targetSum, currentSum
        )
