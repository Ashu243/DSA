import heapq
class KthLargest:

    def __init__(self, k: int, arr):
        self.heap = []
        n = len(arr)
        self.k = k
        for elem in arr:
            if len(self.heap) < k:
                heapq.heappush(self.heap, elem)
            elif elem > self.heap[0]:
                heapq.heapreplace(self.heap, elem)
        

    def add(self, val: int) -> int:
        if len(self.heap) < self.k:
            heapq.heappush(self.heap, val)

        else:
            if val > self.heap[0]:
                heapq.heapreplace(self.heap, val)

        return self.heap[0]

        