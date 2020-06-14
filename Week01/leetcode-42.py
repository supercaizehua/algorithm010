class Solution:
    def trap(self, height: List[int]) -> int:
        left, right = 0, len(height) - 1
        ds = 0
        h = 0

        while left <= right:
            if height[left] < height[right]:
                if height[left] > h:
                    ds += (height[left] - h) * (right - left + 1)
                    h = height[left]
                left += 1
            else:
                if height[right] > h:
                    ds += (height[right] - h) * (right - left + 1)
                    h = height[right]
                right -= 1
                
        return ds - sum(height)
