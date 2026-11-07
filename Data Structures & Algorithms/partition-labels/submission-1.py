class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        counter = Counter(s)
        res = []

        curr_chars = set()
        l, r = 0, 0

        for r in range(len(s)):
            curr_chars.add(s[r])
            counter[s[r]] -= 1
            if counter[s[r]] == 0:
                can_add = True
                for char in curr_chars:
                    if counter[char] > 0:
                        can_add = False
                        break
                if can_add:
                    res.append(r - l + 1)
                    l = r + 1
                    curr_chars = set()

        return res