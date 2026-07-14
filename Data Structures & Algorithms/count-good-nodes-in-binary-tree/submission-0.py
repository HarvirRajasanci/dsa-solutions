# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        def dfs(node, value):
            if not node:
                return 0

            total = 1 if node.val >= value else 0
            curr_value = max(value, node.val)

            total += dfs(node.left, curr_value)
            total += dfs(node.right, curr_value)
            
            return total

        return dfs(root, root.val)