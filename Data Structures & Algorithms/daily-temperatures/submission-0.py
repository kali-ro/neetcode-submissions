class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # stack of indicies
        min_stack = []

        res = [0] * len(temperatures)

        # iterate backwards
        for i in range(len(temperatures) - 1, -1, -1):
            if not min_stack:
                res[i] = 0
                min_stack.append(i)
            else:
                if temperatures[i] < temperatures[min_stack[-1]]:
                    res[i] = min_stack[-1] - i
                    min_stack.append(i)
                elif temperatures[i] >= temperatures[min_stack[-1]]:
                    while min_stack:
                        if temperatures[i] >= temperatures[min_stack[-1]]:
                            min_stack.pop()
                        else:
                            break
                    if min_stack:
                        res[i] = min_stack[-1] - i
                    else:
                        res[i] = 0
                    min_stack.append(i)
        
        return res