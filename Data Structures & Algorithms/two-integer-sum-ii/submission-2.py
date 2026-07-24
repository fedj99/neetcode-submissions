class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        n = len(numbers)
        i = 0
        j = n - 1
        
        while i < j:
            s = numbers[i] + numbers[j]

            # Base case: Sum equals target
            if s == target:
                return [i + 1, j + 1]

            # If sum is greater than target, need to decrease larger element
            if s > target:
                j -= 1

            # If sum is less than target, need to increase smaller element
            elif s < target:
                i += 1

        return [-1, -1]
            