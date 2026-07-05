from _heapq import heapify, heappop
import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        ret = []
        countSet = {}

        for i in nums:
            if i in countSet:
                countSet[i] += 1
            else:
                countSet[i] = 1

        heap = []
        for i in countSet:
            heap.append((-1 * countSet[i], i))

        heapify(heap)

        for i in range(k):
            ret.append(heappop(heap)[1])

        return ret
