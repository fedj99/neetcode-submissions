class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        prefix = [nums[0]] + [-9999] * (n-1)
        suffix = [-9999] * (n-1) + [nums[-1]]
        res = [-9999] * n

        for i in range(1, n):
            num = nums[i]
            prefix[i] = prefix[i-1] * num
        
        for i in range(n - 2, 0, -1):
            num = nums[i]
            suffix[i] = suffix[i+1] * num

        res[0] = suffix[1]
        res[-1] = prefix[-2]

        for i in range(1, n-1):
            res[i] = prefix[i - 1] * suffix[i + 1]
        
        return res