import heapq

class KthLargest:

    heap = []
    kth = 0
    def __init__(self, k: int, nums: List[int]):
        global heap
        self.heap = []
        global kth
        self.kth = k

        for i in nums:
            if len(self.heap) < k:
                heapq.heappush(self.heap, i)
            elif self.heap[0] < i: 
                heapq.heappush(self.heap, i)
                heapq.heappop(self.heap)
            heapq.heapify(self.heap)
        return None

    def add(self, val: int) -> int:
        global heap
        if not self.heap or len(self.heap) < self.kth:
            heapq.heappush(self.heap, val)
        else:
            heapq.heappushpop(self.heap, val)
        heapq.heapify(self.heap)
        return self.heap[0]
