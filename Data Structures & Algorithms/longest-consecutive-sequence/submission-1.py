class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        values = set(nums)
        max_length = 0

        for num in nums:
            if num-1 in values:
                continue
            # Start of sequence, check sequentially until values exhausted
            cur = num
            cur_len = 1
            while cur + 1 in values:
                cur += 1
                cur_len += 1
            max_length = max(max_length, cur_len)

        return max_length
