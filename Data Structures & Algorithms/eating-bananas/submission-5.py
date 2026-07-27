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

        while r - l > 1:
            k = l + (r - l) // 2
            t1 = self.time(k)
            t2 = self.time(k - 1)
            print(f"{l=}, {r=}, {k=}, {t1=}, {t2=}")

            # Base case: t1 is fast enough (<= h) and t2 is too slow (> h) -> we found optimal k
            if t1 <= h and t2 > h:
                print(f">>> t1 fast enough and t2 is too slow, returning")
                return k

            # If t1 is not fast enough, need to increase lower bound
            if t1 > h:
                l = k + 1
                print(f">>> t1 not fast enough, increase lower bound to {l=}")
            
            # If t1 is fast enough, but not optimal, decrease upper bound
            elif t1 <= h:
                r = k
                print(f">>> t1 fast enough but not optimal, decreasing upper bound {r=}")

            # Should never happen
            else:
                assert False, f"Invariant broken: {h=}, {k=} ({t1=}), {k-1=} ({t2=})"
        
        if self.time(l) > h:
            print("No solution!")
            return -1

        return l
                
