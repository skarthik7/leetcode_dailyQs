class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        out_opp = 0
        for word in words:
            for letter in word:
                if letter not in allowed:
                    out_opp += 1
                    break
        return len(words)-out_opp
# time complexity: O(n*m)