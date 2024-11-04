class Solution:
    def compressedString(self, word: str) -> str:
        comp = ""
        while word:
            c = word[0]
            prefix_length = min(9, len(word) - len(word.lstrip(c)))
            comp += str(prefix_length) + c
            word = word[prefix_length:]
        return comp