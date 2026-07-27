import math

class Solution:
    def __init__(self) -> None:
        self.nums: list[int]
    
    def find_rotation(self):
        nums = self.nums
        n = len(nums)
        if n <= 1:
            return len(nums)

        if nums[0] < nums[n-1]:
            return 0

        l = 1
        r = n - 1

        while l <= r:
            k = l + (r - l) // 2

            if nums[k] < nums[k-1]:
                return k
            if nums[k] > nums[-1]:
                l = k + 1
            elif nums[k] < nums[0]:
                r = k - 1
            else:
                assert False, f"Invariant violated: {n=}, {l=}, {r=}, {k=}\nnums={str(nums)}"
        
        return n  # Rotation of n equivalent to no shift, but no division by zero
    
    def search(self, nums: List[int], target: int) -> int:
        n = len(nums)

        if n == 0:
            return -1

        if n == 1:
            return 0 if nums[0] == target else -1

        self.nums = nums
        # Two-step process: 1st, find out rotation k
        # Then find element using binary search and index modulus
        # to search in a rotated array.

        # Find rotation
        print(nums)
        k = self.find_rotation()
        print(f"{k=}")

        # Now binary search in the half of the array that contains the target
        if k == 0:
            l = 0
            r = n-1
        elif nums[0] <= target <= nums[k - 1]:
            l = 0
            r = k - 1
        elif nums[k] <= target <= nums[n-1]:
            l = k
            r = n - 1
        else:
            return -1 # Not in range

        while l <= r:
            m = l + (r - l) // 2
            if nums[m] == target:
                return m
            if nums[m] > target:
                r = m - 1
            elif nums[m] < target:
                l = m + 1
            else:
                assert False
        
        return -1

