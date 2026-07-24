class Solution:
    def maxArea(self, heights: List[int]) -> int:
        n = len(heights)
        i = 0
        j = n - 1
        max_V = 0

        while i < j:
            hi, hj = heights[i], heights[j]
            V = (j - i) * min(hi, hj)
            max_V = max(V, max_V)
            if hi <= hj:
                i += 1
            else:
                j -= 1

        return max_V