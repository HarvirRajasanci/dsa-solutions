# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []

        q = deque([root])
        reverse = False
        res = []
        while q:
            size = len(q)
            level = []
            for i in range(size):
                node = q.popleft()
                level.append(node.val)
                q.append(node.left) if node.left else None
                q.append(node.right) if node.right else None

            if reverse:
                res.append(level[::-1])
            else:
                res.append(level)
            reverse = not reverse
        return res
