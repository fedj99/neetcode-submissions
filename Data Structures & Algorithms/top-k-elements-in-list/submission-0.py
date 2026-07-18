class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freqs = defaultdict(lambda: 0)
        for num in nums:
            freqs[num] += 1

        buckets = defaultdict(list)
        for num, freq in freqs.items():
            buckets[freq].append(num)

        res = []
        f = len(nums)
        while len(res) < k and f > 0:
            res.extend(buckets[f])
            f -= 1

        return res