class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)

        triplets = set()

        # First, sort, so we can use two pointers algo
        nums = sorted(nums)
        # print("Sorted:", nums)

        # Iterate over first element
        i = 0
        while i < n:
            a = nums[i]  # Negative target for sum of other two
            # print(f"Case: nums[{i}] = {a}")

            j = i + 1
            k = n - 1

            while j < k:
                b, c = nums[j], nums[k]
                s = b + c
                # print(f">>> {i=} {j=} {k=} | {a=} {b=} {c=} {s=} \t", end=None)

                if s == -a:
                    # print(f">>> euqal, add {a, b, c}; break")
                    triplets.add((a, b, c))
                    # Since we don't care about duplicates, we can just break now
                    j += 1
                    k -= 1
                elif s > -a:
                    k -= 1
                    # print(f">>> s > -a, advance k (--), {k=}")
                elif s < -a:
                    j += 1
                    # print(f">>> s < -a, advance j (++), {j=}")
            
            # Advance i
            i += 1
            # print(f">>> advance i (++), {i=}")

        return [list(x) for x in triplets]