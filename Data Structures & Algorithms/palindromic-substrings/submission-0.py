class Solution:
    def countSubstrings(self, s: str) -> int:
        res = 0

        for i in range(len(s)):
            palis = self.helper(s, i)
            res += palis

        return res
    
    def helper(self, s, i):
        l, r = i, i
        palis = 0
        while l >= 0 and r < len(s) and s[l] == s[r]:
            palis += 1
            l -= 1
            r += 1

        l, r = i, i + 1
        while l >= 0 and r < len(s) and s[l] == s[r]:
            palis += 1
            l -= 1
            r += 1
            
        return palis