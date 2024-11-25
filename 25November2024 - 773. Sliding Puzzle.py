#https://leetcode.com/problems/sliding-puzzle/
class Solution:
    def slidingPuzzle(self, board: List[List[int]]) -> int:
        start = ''.join(str(num) for row in board for num in row)
        target = "123450"
        
        moves = {
            0: [1, 3],
            1: [0, 2, 4],
            2: [1, 5],
            3: [0, 4],
            4: [1, 3, 5],
            5: [2, 4]
        }
        
        # bfs
        queue = deque([(start, 0)])  # (state, moves)
        seen = {start}
        
        while queue:
            state, steps = queue.popleft()
            
            if state == target:
                return steps
            
            zero_pos = state.index('0')
            
            for next_pos in moves[zero_pos]:
                new_state = list(state)
                new_state[zero_pos], new_state[next_pos] = new_state[next_pos], new_state[zero_pos]
                new_state = ''.join(new_state)
                
                if new_state not in seen:
                    seen.add(new_state)
                    queue.append((new_state, steps + 1))
        
        return -1
# Time Complexity: O(N!)