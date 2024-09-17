class Solution:
    def uncommonFromSentences(self, s1: str, s2: str) -> List[str]:
        words = s1.split() + s2.split()
        counter = Counter(words)
        return [word for word in counter if counter[word] == 1]

# Time complexity: O(n)