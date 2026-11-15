class Solution:
    def maxArea(self, heights: List[int]) -> int:
        left = 0
        right = len(heights) - 1 
        volume = 0 
        while left < right:
            volume = max(min(heights[left], heights[right]) * (right - left), volume)
            if heights[left] < heights[right]:
                left += 1 
            else:
                right -= 1 

        return volume