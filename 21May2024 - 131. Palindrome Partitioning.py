class Solution:
    def partition(self, s: str) -> List[List[str]]:
        def isPalindrome(s):
            return s == s[::-1]

        def dfs(start, path):
            if start == len(s):
                result.append(path)
                return
            for end in range(start + 1, len(s) + 1):
                if isPalindrome(s[start:end]):
                    dfs(end, path + [s[start:end]])

        result = []
        dfs(0, [])
        return result