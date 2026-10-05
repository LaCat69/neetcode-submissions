class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        memo = {}
        length = len(s)

        def dfs(i):
            if i == len(s):
                return True
            if i in memo:
                return memo[i]
            
            for w in wordDict:
                if s[i] == w[0]:
                    word_len = len(w)
                    if i + word_len <= length and s[i: i + word_len] == w:
                        if dfs(i + word_len):
                            memo[i] = True
            if i not in memo:
                memo[i] = False
            
            return memo[i]

        return dfs(0)