class Solution:
    def countOfAtoms(self, formula: str) -> str:
        
        import re
        from collections import defaultdict

        def parse(formula):
            stack = [defaultdict(int)]
            i, n = 0, len(formula)

            while i < n:

                if formula[i] == '(':
                    stack.append(defaultdict(int))
                    i += 1

                elif formula[i] == ')':
                    i += 1
                    i_start = i
                    while i < n and formula[i].isdigit():
                        i += 1
                    count = int(formula[i_start:i] or 1)
                    top = stack.pop()
                    for atom, atom_count in top.items():
                        stack[-1][atom] += atom_count * count

                else:
                    i_start = i
                    i += 1
                    while i < n and formula[i].islower():
                        i += 1
                    atom = formula[i_start:i]
                    i_start = i
                    while i < n and formula[i].isdigit():
                        i += 1
                    count = int(formula[i_start:i] or 1)
                    stack[-1][atom] += count


            return stack[-1]

        counts = parse(formula)


        return ''.join(f"{atom}{(count if count > 1 else '')}" for atom, count in sorted(counts.items()))
        
# Time complexity: O(N) as we iterate through the formula once where N is the length of the formula.