class Solution:
    def __init__(self) -> None:
        self.h: int
        self.piles: list[int]
    
    def time(self, k: int):
        if k == 0:
            return float('inf')
        tot_h = 0
        for b in self.piles:
            tot_h += math.ceil(b / k)
        return tot_h

    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        self.piles = piles
        self.h = h
        
        m = max(piles)

        l = 1
        r = m

        k_min = r

        while l <= r:
            k = l + (r - l) // 2
            t = self.time(k)

            if t <= h:
                # Valid, record, lower upper bound
                k_min = min(k_min, k)
                r = k - 1
            else:  # t > h
                l = k + 1
        
        if self.time(l) > h:
            print("No solution!")
            return -1

        return l
                
