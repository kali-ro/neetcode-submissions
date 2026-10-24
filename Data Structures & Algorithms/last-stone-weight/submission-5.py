class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heap = stones
        heapq.heapify_max(heap)
        while len(heap) > 1:
            x = heapq.heappop_max(heap)
            y = heapq.heappop_max(heap)

            if x == y:
                continue
            elif x < y:
                heapq.heappush_max(heap, y-x)
            elif x > y:
                heapq.heappush_max(heap, x-y)

        if not heap:
            return 0
        else:
            return heap[0]