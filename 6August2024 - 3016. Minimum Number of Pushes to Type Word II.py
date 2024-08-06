from collections import Counter

class Solution:
    def minimumPushes(self, word: str) -> int:
        counts = Counter(word)
        countsSorted = sorted(counts.values(), reverse=True)
        res = 0
        for i, count in enumerate(countsSorted):
            res += (i // 8 + 1) * count
        return res

# Time complexity: O(n) because we iterate through the word string once.