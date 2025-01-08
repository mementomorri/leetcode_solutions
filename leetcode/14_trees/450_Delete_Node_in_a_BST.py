# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        if not root:
            return root

        if root.val < key:
            root.right = self.deleteNode(root.right, key)
        elif root.val > key:
            root.left = self.deleteNode(root.left, key)
        else:
            if root.left == None:
                return root.right
            elif root.right == None:
                return root.left
            else:
                minNode = self.minValueNode(root.right)
                root.val = minNode.val
                root.right = self.deleteNode(root.right, minNode.val)
        return root

    def minValueNode(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        current = root
        while current and current.left:
            current = current.left
        return current
