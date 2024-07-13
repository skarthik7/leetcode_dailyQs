from collections import deque

class Solution:
    def survivedRobotsHealths(self, positions, healths, directions):
        robots = list(zip(positions, healths, directions, range(len(positions))))
        robots.sort()  # Sort based on positions
        stack = []

        for pos, health, direction, idx in robots:
            if direction == 'R':
                stack.append((pos, health, direction, idx))
            else:  # direction == 'L'
                while stack and stack[-1][2] == 'R' and stack[-1][1] < health:
                    _, h, _, i = stack.pop()
                    health -= 1
                if stack and stack[-1][2] == 'R' and stack[-1][1] == health:
                    stack.pop()
                elif stack and stack[-1][2] == 'R' and stack[-1][1] > health:
                    pos_r, health_r, direction_r, idx_r = stack.pop()
                    stack.append((pos_r, health_r - 1, direction_r, idx_r))
                else:
                    stack.append((pos, health, direction, idx))

        result = [-1] * len(positions)
        for pos, health, direction, idx in stack:
            result[idx] = health

        return [h for h in result if h != -1]
# Time complexity: O(N) as we iterate through the robots once where N is the number of robots.