class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # build index map
        idx = {v: i for i, v in enumerate(nums)}
        for i, num in enumerate(nums):
            c = target - num
            if c in idx and idx[c] != i:
                return [i, idx[c]]
        
        return []