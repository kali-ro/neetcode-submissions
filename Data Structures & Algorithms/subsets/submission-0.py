class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []

        def backtrack(index, path):
            # base case, store a copy of path
            if index == len(nums):
                res.append(path.copy())
                return

            # add num to path and call backtrack
            path.append(nums[index])
            backtrack(index + 1, path)

            # remove num and call backtrack (do nothing branch)
            path.pop()
            backtrack(index + 1, path)
        
        # start the recursion
        backtrack(0, [])
        return res