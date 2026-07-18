class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        for s in strs:
            header = chr(len(s)) # Constraint: 0 <= n < 200
            res += header + s
        return res

    def decode(self, s: str) -> List[str]:
        res = []
        while s:
            n, s = ord(s[0]), s[1:]
            t, s = s[:n], s[n:]
            res.append(t)
        return res
