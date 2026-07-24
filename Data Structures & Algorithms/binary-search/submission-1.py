class Solution:
    def search(self, nums: List[int], target: int) -> int:
        n = len(nums)
        l = 0
        r = n

        while (r - l) > 1: 
            m = (l + r) // 2

            if target < nums[m]:
                r = m
            elif target > nums[m]:
                l = m
            else:
                return m

        if nums[l] == target:
            return l
        
        return -1