class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        output = []
        if sum(candidates) < target:
            return []
        if sum(candidates) == target:
            return [candidates]
        candidates.sort()
        
        def backtrack(current, position, target):
            if target == 0:
                output.append(current.copy())
            if target <=0:
                return
            prev = -1
            for i in range(position, len(candidates)):
                if candidates[i] == prev:
                    continue
                current.append(candidates[i])
                backtrack(current,i+1,target-candidates[i])
                current.pop()
                prev = candidates[i]


        backtrack([],0,target)
        return output