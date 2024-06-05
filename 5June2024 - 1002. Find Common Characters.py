class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        output = []
        for letter in words[0]:
            there = True
            for i in range(1,len(words)):
                if letter not in words[i]:
                    there = False
                else:
                    words[i] = words[i].replace(letter,"9",1)
            words[0]=words[0].replace(letter,"9",1)
            print(words)
            if there == True:
                output.append(letter)
        return output