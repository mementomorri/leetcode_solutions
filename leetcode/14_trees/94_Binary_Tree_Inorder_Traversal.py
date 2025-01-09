class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        def _helper(root, data):
            if not root:
                return
            _helper(root.left, data)
            data.append(root.val)
            _helper(root.right, data)

        data = []
        _helper(root, data)
        return data
