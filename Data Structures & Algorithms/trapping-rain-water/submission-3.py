class Solution:
    def trap(self, height: List[int]) -> int:
        left, right = 0, len(height) - 1
        left_max, right_max = height[left], height[right]
        max_area = 0
        
        while left < right:
            if left_max < right_max:
                left += 1
                max_area += max(left_max - height[left], 0)
                left_max = max(left_max, height[left])
            else:
                right -= 1
                max_area += max(right_max - height[right], 0)
                right_max = max(right_max, height[right])

        return max_area
