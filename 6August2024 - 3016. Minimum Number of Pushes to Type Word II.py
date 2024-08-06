from collections import Counter

class Solution:
    def minimumPushes(self, word: str) -> int:
        frequency = Counter(word)
        
        sorted_letters = sorted(frequency.items(), key=lambda x: -x[1])
        
        pushes = {}
        key_position = 1
        for letter, freq in sorted_letters:
            pushes[letter] = key_position
            key_position += 1
            if key_position > 3:
                key_position = 1
        
        total_pushes = 0
        for letter in word:
            total_pushes += pushes[letter]
        
        return total_pushes