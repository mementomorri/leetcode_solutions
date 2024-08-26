"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""


class Solution:
    def postorder_recursive(self, root: "Node") -> List[int]:
        # time(O(n))
        # space(O(h)) - h for height of tree
        def helper(node):
            if not node:
                return
            for c in node.children:
                helper(c)
            res.append(node.val)

        res = []
        helper(root)
        return res

    def postorder(self, root: "Node") -> List[int]:
        # time(O(n))
        # space(O(h)) - h for height of tree
        res = []
        if not root:
            return []
        stack = [(root, False)]

        while stack:
            node, visited = stack.pop()
            if visited:
                res.append(node.val)
            else:
                stack.append((node, True))
                for c in node.children[::-1]:
                    stack.append((c, False))
        return res
