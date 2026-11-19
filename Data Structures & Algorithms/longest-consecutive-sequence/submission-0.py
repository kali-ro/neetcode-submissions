class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        num_set = set()
        for num in nums:
            num_set.add(num)

        res = 0
        for num in num_set:
            if num - 1 not in num_set:
                l = 1
                curr = num
                while curr + 1 in num_set:
                    curr += 1
                    l += 1
                res = max(res, l)

        return res



        