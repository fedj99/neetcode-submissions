class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        for c in set(s) | set(t):
            cs = sum(1 for d in s if d == c)
            ct = sum(1 for d in t if d == c)
            if cs != ct:
                return False
        return True