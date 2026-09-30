class Solution:
    def longestPalindrome(self, s: str) -> str:
        res = (0, 0)

        for i in range(len(s)):
            pali = self.helper(s, i)
            if pali[1] - pali[0] > res[1] - res[0]:
                res = pali

        return s[res[0]:res[1]]
    
    def helper(self, s, i):
        l, r = i, i
        pali = (l, r+1)
        while l >= 0 and r < len(s) and s[l] == s[r]:
            if pali[1] - pali[0] < r + 1 - l:
                pali = (l, r+1)
            l -= 1
            r += 1

        l, r = i, i + 1
        while l >= 0 and r < len(s) and s[l] == s[r]:
            if pali[1] - pali[0] < r + 1 - l:
                pali = (l, r+1)
            l -= 1
            r += 1
            
        return pali