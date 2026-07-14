# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        p_queue = deque([p])
        q_queue = deque([q])

        while p_queue and q_queue:
            for i in range(len(p_queue)):
                p_node = p_queue.popleft()
                q_node = q_queue.popleft()

                if p_node is None and q_node is None:
                    continue

                if p_node is None or q_node is None or p_node.val != q_node.val:
                    return False

                p_queue.append(p_node.left)
                p_queue.append(p_node.right)
                q_queue.append(q_node.left)
                q_queue.append(q_node.right)

        return True