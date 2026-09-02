# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []

        q = deque([root])
        level_ordered_list = []
        while q:
            size = len(q)
            current_level_elements = []

            for i in range(size):
                node = q.popleft()
                current_level_elements.append(node.val)

                q.append(node.left) if node.left else None
                q.append(node.right) if node.right else None

            level_ordered_list.append(current_level_elements)
        return level_ordered_list