class Solution:
    def clean(self, s: str):
        """Transforms to lowercase and removes any non-alphanumeric characters"""
        # Could also be done using regex but that's overkill
        # Or using a fixed string to check for valid characters
        return "".join([
            c for c in s.lower() 
            if ord("a") <= ord(c) <= ord("z")
            or ord("0") <= ord(c) <= ord("9")
        ])

    def isPalindrome(self, s: str) -> bool:
        # Get clean string first, without spaces and special characters and punctuation
        s_clean = self.clean(s)

        # Check that it's the same from front or back, only need to check to middle
        for i in range(len(s_clean) // 2):
            j = len(s_clean) - i - 1
            if s_clean[i] != s_clean[j]:
                return False
        return True