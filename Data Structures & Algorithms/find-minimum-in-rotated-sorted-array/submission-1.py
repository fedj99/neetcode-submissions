class Solution:
    def findMin(self, nums: List[int]) -> int:
        n = len(nums)

        # Edge case: Empty array
        if n == 0:
            return 0
        
        # Edge case: Length 1
        if n == 1:
            return nums[0]

        # Edge case: If nums[0] < nums[n-1]: Already sorted, k == n
        if nums[0] < nums[n-1]:
            return nums[0]

        # Find the k such that nums[k % n] < nums[(k-1) % n]
        # Normally should be the opposite, but will be true
        # when array wraps around.
        #
        # Since all values are unique, no need to worry about
        # equal values.
        #
        # To determine what side of the minimum we are, we split
        # the array in three parts:
        #
        # |       A         | min |       B        |
        # 
        # and we note that A > B, and B < A
        # 
        # So if we pick a k in A, we know we are left of the minimum,
        # and should rotate more, so increase the lower bound
        #
        # Conversely, if we pick k in B, we are to the right of the
        # minimum, and should lower the upper bound.
        # 
        # To know whether k is in A or B, check: If nums[k] > nums[n-1],
        # k must be in A, since nums[n-1] is the largest value in B
        # and we have A > B. Similarly, we are in B if nums[k] < nums[0].
        #
        # We choose to handle the edge case k = n separately, so that 
        # we have k in {1, ... n-1}. k = 0 does not appear as per task 
        # description but is indistinguishable from k = n.

        l = 1
        r = n-1

        k = -1

        while l <= r:
            k = l + (r - l) // 2

            if nums[k] < nums[k - 1]:
                # We found the minimum
                return nums[k]

            if nums[k] > nums[n - 1]:
                # We are in A, increase lower bound
                l = k + 1
            elif nums[k] < nums[0]:
                # We are in B, decrease upper bound
                r = k - 1
            else:
                assert False, "Invariant failure"

        assert False, "No solution"
