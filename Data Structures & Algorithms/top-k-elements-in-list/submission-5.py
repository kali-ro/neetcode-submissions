class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dic = {}
        counts = [[] for i in range(len(nums) + 1)]

        for n in nums:
            dic[n] = 1 + dic.get(n, 0)
        
        for val, count in dic.items():
            counts[count].append(val)
        
        res = []
        for i in range(len(counts) - 1, 0, -1):
            for num in counts[i]:
                res.append(num)
                if k == len(res):
                    return res