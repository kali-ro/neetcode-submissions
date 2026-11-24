class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # stack of indicies
        min_stack = []
        res = [0] * len(temperatures)

        for i, t in enumerate(temperatures):
            while min_stack and t > min_stack[-1][0]:
                stackT, stackInd = min_stack.pop()
                res[stackInd] = i - stackInd
            min_stack.append((t, i))        
        return res