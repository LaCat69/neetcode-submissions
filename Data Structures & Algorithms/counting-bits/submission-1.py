class Solution:
    def countBits(self, n: int) -> List[int]:
        output = []
        for num in range(n + 1):
            output.append(num.bit_count())
        return output