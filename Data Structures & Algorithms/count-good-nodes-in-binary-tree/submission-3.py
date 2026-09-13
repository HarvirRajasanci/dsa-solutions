# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        def dfs(node, greatest):
            if not node:
                return 0
            
            total = 1 if node.val >= greatest else 0
            greatest = max(greatest, node.val)

            total += dfs(node.left, greatest)
            total += dfs(node.right, greatest)
            return total

        return dfs(root, root.val)