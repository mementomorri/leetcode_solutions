class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        res = []
        q = []
        if root:
            q.append(root)

        level = 0
        while q:
            res.append([])
            q_len = len(q)
            for _ in range(q_len):
                cur = q.pop(0)
                res[level].append(cur.val)
                if cur.left:
                    q.append(cur.left)
                if cur.right:
                    q.append(cur.right)
            level += 1

        return res
