class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        for i, a in enumerate(numbers):
            for k, b in enumerate(numbers[i+1:]):
                j = i + 1 + k
                if a + b == target:
                    # found
                    return [i + 1, j + 1]