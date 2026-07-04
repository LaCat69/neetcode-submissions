class Solution:

    def encode(self, strs: List[str]) -> str:
        result = ""
        for char in strs:
            result += f"{len(char)}#" + char
        return result

    def decode(self, s: str) -> List[str]:
        i = 0
        result = []
        gap = ""
        while i < len(s)-1:
            while s[i].isdigit():
                gap += s[i]
                i += 1
            result.append(s[i+1:int(gap)+i+1])
            i += int(gap) + 1
            gap = ""
        return result