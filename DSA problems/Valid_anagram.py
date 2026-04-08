class Solution:
    """Solve string anagram checks."""

    def is_anagram(self, s: str, t: str) -> bool:
        """Return True if s and t are anagrams of each other."""
        if len(s) != len(t):
            return False

        freq = {}
        for ch in s:
            freq[ch] = freq.get(ch, 0) + 1

        for ch in t:
            if ch not in freq:
                return False
            freq[ch] -= 1
            if freq[ch] < 0:
                return False

        return True
solution = Solution()
result  = solution.is_anagram("anagra", "nagaram")
print(result)