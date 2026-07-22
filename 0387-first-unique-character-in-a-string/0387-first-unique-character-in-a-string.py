class Solution:
    def firstUniqChar(self, s: str) -> int:
        from collections import Counter
        freq = Counter(s)   # Step 1: count frequencies
        for i, ch in enumerate(s):  # Step 2: find first unique
            if freq[ch] == 1:
                return i
        return -1