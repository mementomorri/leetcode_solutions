class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        res = []

        queue = []
        if root:
            queue.append(root)

        cur = root
        prev = cur
        while queue:
            q_len = len(queue)
            for _ in range(q_len):
                cur = queue.pop(0)
                if cur.left:
                    queue.append(cur.left)
                if cur.right:
                    queue.append(cur.right)
                prev = cur
            res.append(prev.val)

        return res
