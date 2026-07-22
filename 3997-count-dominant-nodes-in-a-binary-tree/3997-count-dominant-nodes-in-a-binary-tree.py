# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countDominantNodes(self, root: TreeNode | None) -> int:
        def dfs(node):
            if not node:
                return 0

            m = max(dfs(node.left), dfs(node.right))
            if node.val >= m:
                self.t += 1

            return max(m, node.val)

        self.t = 0
        dfs(root)
        return self.t