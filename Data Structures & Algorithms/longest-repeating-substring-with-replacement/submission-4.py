class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        chars = {}
        mf = 0
        l = 0
        max_length = 0
        for r in range(len(s)):
            chars[s[r]] = chars.get(s[r], 0) + 1
            if chars[s[r]] > mf:
                mf = chars[s[r]]
            while mf + k < r - l + 1:
                chars[s[l]] -= 1
                l += 1
            max_length = max(max_length, r - l + 1)
        return max_length
