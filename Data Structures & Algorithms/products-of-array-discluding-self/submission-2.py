class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        total = 1
        num0s = 0
        for n in nums:
            if n != 0:
                total = total * n
            else:
                num0s += 1
        i = 0
        while i < len(nums):
            if num0s == 1:
                if nums[i] == 0:
                    nums[i] = total
                else:
                    nums[i] = 0
            elif num0s > 1:
                nums[i] = 0
            else:
                temp = nums[i]
                nums[i] = total // temp
            i += 1

        return nums