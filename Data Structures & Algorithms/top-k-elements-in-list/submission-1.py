import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        heap_list = []
        hashmap = {}
        for i in nums:
            hashmap[i] = hashmap.get(i,0) + 1

        for num , count in hashmap.items():
            heapq.heappush(heap_list , (count , num))

            if len(heap_list) > k:
                heapq.heappop(heap_list)

        return [x[1] for x in heap_list]

