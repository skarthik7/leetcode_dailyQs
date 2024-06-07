class Solution:
    def replaceWords(self, dictionary: List[str], sentence: str) -> str:
        rootset = set(dictionary)

        def replace(word):
            for i in range(1, len(word)):
                if word[:i] in rootset:
                    return word[:i]
            return word

        return ' '.join(map(replace, sentence.split()))
    
# Time complexity: O(N * M) where N is the length of the sentence and M is the length of the longest word in the dictionary
# Space complexity: O(N) where N is the length of the sentence