class Solution:
    def findMedianSortedArrays(self, a: List[int], b: List[int]) -> float:
        if len(b) < len(a):
            a, b = b, a

        length_a, length_b = len(a), len(b)
        total = length_a + length_b
        half = total // 2
        l, r = 0, length_a - 1
            

        while True:
            i = (l + r) // 2
            j = half - i - 2
            a_left = a[i] if i >= 0 else float("-inf")
            a_right = a[i+1] if i+1 < length_a else float("inf")
            b_left = b[j] if j >= 0 else float("-inf")
            b_right = b[j+1] if j+1 < length_b else float("inf")

            if a_left <= b_right and b_left <= a_right:
                if total % 2:
                    return min(a_right, b_right)
                return (max(a_left, b_left) + min(a_right, b_right)) / 2
                
            elif a_left > b_right:
                r = i - 1
            else:
                l = i + 1