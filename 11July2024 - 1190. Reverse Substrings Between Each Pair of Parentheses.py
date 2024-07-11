class Solution:
    def reverseParentheses(self, s: str) -> str:
        stack = []
        for char in s:
            if char == ')':
                temp = ''
                while stack[-1] != '(':
                    temp += stack.pop()
                stack.pop() 
                for item in temp:
                    stack.append(item)
            else:
                stack.append(char)
        return ''.join(stack)
    
# Time complexity: O(N) as we iterate through the string once where N is the length of the string.