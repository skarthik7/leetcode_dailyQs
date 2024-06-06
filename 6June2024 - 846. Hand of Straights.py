class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        freq = {}
        for card in hand:
            freq[card] = freq.get(card, 0) + 1
        sorted_hand = sorted(hand)
        for card in sorted_hand:
            if freq[card] == 0:
                continue
            for i in range(groupSize):
                if freq.get(card + i, 0) == 0:
                    return False
                freq[card + i] -= 1
        return True