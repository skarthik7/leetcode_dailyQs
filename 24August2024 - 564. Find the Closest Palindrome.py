class Solution:
    def nearestPalindromic(self, n: str) -> str:
        length = len(n)
        num = int(n)
        
        if num <= 10 or (num == 10**(length-1)):
            return str(num - 1)
        if num == 10**length - 1:
            return str(num + 2)
        
        candidates = set()
        
        prefix = int(n[:(length + 1) // 2])
        
        for i in [-1, 0, 1]:
            new_prefix = str(prefix + i)
            if length % 2 == 0:
                candidate = new_prefix + new_prefix[::-1]
            else:
                candidate = new_prefix + new_prefix[-2::-1]
            candidates.add(int(candidate))
        
        candidates.add(10**(length - 1) - 1)
        candidates.add(10**length + 1)
        
        candidates.discard(num)
        
        closest_palindrome = min(candidates, key=lambda x: (abs(x - num), x))
        
        return str(closest_palindrome)