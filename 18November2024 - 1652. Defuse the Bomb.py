#https://leetcode.com/problems/defuse-the-bomb/description/


class Solution:
    def decrypt(self, code: List[int], k: int) -> List[int]:
        n=len(code)
        code=code+code
        if k>0:
            resArr=[]
            for i in range(0,n):
                resArr.append(sum(code[i+1:i+k+1]))
            return resArr
        elif k<0:
            k = -k
            for i in range(n*2-1, 0, -1):
                code[i] = sum(code[i-k:i])
            return(code[n:])
        else:
            return [0]*n