class Solution:
    def next_smaller(self, heights: list[int]):
        n = len(heights)
        next_smaller = [n] * n
        stack = []
        
        # Traverse array in reverse order
        for i in range(n - 1, -1, -1):
            h = heights[i]

            while stack and heights[stack[-1]] >= h:
                stack.pop()

            if stack:
                next_smaller[i] = stack[-1]

            stack.append(i)

        return next_smaller

    def prev_smaller(self, heights: list[int]):
        n = len(heights)
        prev_smaller = [-1] * n
        stack = []
        
        # Traverse array forward
        for i, h in enumerate(heights):
            while stack and heights[stack[-1]] >= h:
                stack.pop()

            if stack:
                prev_smaller[i] = stack[-1]

            stack.append(i)

        return prev_smaller

    def largestRectangleArea(self, heights: List[int]) -> int:
        prev_smaller = self.prev_smaller(heights)
        next_smaller = self.next_smaller(heights)

        print(f"{heights=}, {prev_smaller=}, {next_smaller=}")

        max_area = -1

        # Iterate through array and get max size using prev and next smaller
        for i, h in enumerate(heights):
            l = prev_smaller[i]
            r = next_smaller[i]
            w = r - l - 1
            area = w * h
            max_area = max(max_area, area)
            print(f">>> {i=}, {h=}, {l=}, {r=}, {w=}, {area=}")

        return max_area