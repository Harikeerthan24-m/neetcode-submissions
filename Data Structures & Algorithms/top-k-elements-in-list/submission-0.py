class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hashmap = {}
        for i in nums:
            hashmap[i] = hashmap.get(i,0)+1

        # sort by freq
        sorted_dict = sorted(hashmap.items(),key=lambda x:x[1],reverse = True)
        top_k_elements = [i[0] for i in sorted_dict[:k]]
        return top_k_elements
        