class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        result = [-1] * len(temperatures)
        stack = []

        for i, x in enumerate(temperatures):
            # Start of sequence, don't know yet
            if len(stack) == 0:
                stack.append((i, x))
                print(f"empty stack {i, x}")
                print(f">>> push {i, x}")
                continue
            
            # Monotonically non-increasing, add to stack
            if x <= stack[-1][1]:
                stack.append((i, x))
                print(f"decreasing {i, x}")
                print(f">>> push {i, x}")
                continue

            # x > stack[-1], larger than at least one element
            # pop as long as x > stack[-1]
            print(f"increasing, backtrack {i, x}")
            while len(stack) > 0 and stack[-1][1] < x:
                j, y = stack.pop()
                print(f">>> pop {j, y}")
                result[j] = i - j
                print(f">>> result[{j}] = {i - j}")
            stack.append((i, x))
            print(f">>> push {i, x}")

        # All remaining items don't have a larger element in future (all non-increasing)
        # Set all to 0
        print("leftovers")
        while len(stack) > 0:
            j, y = stack.pop()
            print(f">>> pop {j, y}")
            result[j] = 0
            print(f">>> result[{j}] = 0")

        return result
