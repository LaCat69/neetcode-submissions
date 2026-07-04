class Solution:

    def encode(self, strs: List[str]) -> str:
        result = ""
        for char in strs:
            result += f"{len(char)}#" + char
        return result

    def decode(self, s: str) -> List[str]:
        i = 0
        result = []
        while i < len(s):
            gap = ""
            while s[i].isdigit():
                gap += s[i]
                i += 1
            i += 1
            int_gap = int(gap)
            result.append(s[i:int_gap+i])
            i += int(gap)
        return result