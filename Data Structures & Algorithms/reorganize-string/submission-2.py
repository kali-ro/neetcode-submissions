class Solution:
    def reorganizeString(self, s: str) -> str:
        dic = {}
        for c in s:
            dic[c] = dic.get(c, 0) + 1

        heap = [(count, char) for char, count in dic.items()]
        heapq.heapify_max(heap)
        res = ""
        i = 0
        prev = None
        curr = None
        while i < len(s):
            if heap:
                curr = heapq.heappop_max(heap)
            if prev and prev[0] > 0:
                heapq.heappush_max(heap, prev)
            res += curr[1]
            count = curr[0] - 1
            letter = curr[1]
            prev = (count, letter)
            i += 1
        print(res)
        if prev and prev[0] > 0:
            return ""

        return res