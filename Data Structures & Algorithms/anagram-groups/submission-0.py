class Solution:
    def computeFreqs(self, s: str) -> tuple[str, ...]:
        out = [0] * 26
        for c in s:
            i = ord(c) - ord('a')
            out[i] += 1
        return tuple(out)
    
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        out = defaultdict(list)

        for s in strs:
            key = self.computeFreqs(s)
            out[key].append(s)

        return list(out.values())