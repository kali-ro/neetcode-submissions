class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []

        def backtrack(index, path):
            total = sum(path)

            if total == target:
                res.append(path.copy())
                return
            elif total > target or index == len(nums):
                return

            # 3 choices: skip to next number, add same number
            backtrack(index + 1, path)

            path.append(nums[index])
            backtrack(index, path)
            path.pop()

        backtrack(0, [])
        return res