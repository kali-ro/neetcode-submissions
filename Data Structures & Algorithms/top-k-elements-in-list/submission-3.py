class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # get the frequencies
        freq = defaultdict(int)
        for n in nums:
            freq[n] += 1

        buckets = [[] for _ in range(len(nums) + 1)]
        for index, val in freq.items():
            buckets[val].append(index)

        res = []
        for i in range(len(buckets) - 1, 0, -1):
            for num in buckets[i]:
                res.append(num)
                if len(res) == k:
                    return res
        
        return []