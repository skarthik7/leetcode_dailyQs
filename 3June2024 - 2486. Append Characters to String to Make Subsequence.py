class Solution:
    def minCharacters(self, s: str, t: str) -> int:
        i = j = 0
        appended = 0
        while j < len(t):
            if i < len(s) and s[i] == t[j]:
                i += 1
            else:
                appended += 1
            j += 1
        return appended