class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        d = {}

        for i,n in enumerate(nums):
            if n in d:
                return True
            d[n] = i
        
        return False
        


        