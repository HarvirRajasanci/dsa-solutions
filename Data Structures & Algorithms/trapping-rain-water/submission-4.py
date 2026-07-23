class Solution:
    def trap(self, height: List[int]) -> int:
        L, R = 0, len(height) - 1
        leftMax, rightMax = height[L], height[R]
        max_area = 0

        while L < R:
            if leftMax < rightMax:
                L += 1
                leftMax = max(leftMax, height[L])
                max_area += leftMax - height[L]
            else:
                R -= 1
                rightMax = max(rightMax, height[R])
                max_area += rightMax - height[R]

        return max_area
