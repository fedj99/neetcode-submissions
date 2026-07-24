class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m_flat = [x for row in matrix for x in row]  # O(mn)

        # Binary search flat matrix
        l = 0
        r = len(m_flat) - 1

        while l <= r:
            m = l + (r - l) // 2  # Avoid overflow
            if target < m_flat[m]:
                r = m - 1
            elif target > m_flat[m]:
                l = m + 1
            else:
                return True
        
        return False
