class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hash = {}
        for k , v in enumerate(nums):
            comp = target - v
            if comp in hash:
                return list((hash[comp] , k))
            hash[v] = k 