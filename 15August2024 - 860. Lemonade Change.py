class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        currentFives = 0
        currentTens = 0
        currentTwenties = 0
        for bill in bills:
            if bill == 5:
                currentFives+=1
            elif bill == 10:
                currentTens += 1
                if currentFives == 0:
                    return False
                else:
                    currentFives-=1
            elif bill == 20:
                if currentFives > 0 and currentTens > 0:
                    currentFives -= 1
                    currentTens -= 1
                elif currentFives > 2 :
                    currentFives -= 3
                else:
                    return False
        return True


# Time complexity: O(n) as we are iterating through the bills array once.