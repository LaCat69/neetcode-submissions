class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        hand.sort()
        counter = Counter(hand)

        for n in hand:
            if counter[n] == 0:
                continue
            for mem in range(n, n + groupSize):
                counter[mem] -= 1
                if counter[mem] < 0:
                    return False

        return True