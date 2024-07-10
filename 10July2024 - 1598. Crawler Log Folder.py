class Solution:
    def minOperations(self, logs: List[str]) -> int:
        depth = 0

        for log in logs:
            if log == "../":
               
                if depth > 0:
                    depth -= 1
            elif log == "./":
                continue
            else:
                depth += 1

        return depth

# Time complexity: O(N) as we iterate through the logs once where N is the number of logs in the list.