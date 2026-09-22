class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        count = 1
        longest = 1 
        # sort the values
        nums.sort()

        n = len(nums)

        # 0 check 
        if n == 0:
            return 0 

        # loop 
        for i in range(n):
            # previous value check 
            if i < 1:
                continue
            # duplicate check 
            elif nums[i-1] == nums[i]:
                continue
            # core check 
            elif nums[i-1] + 1 == nums[i]:
                count += 1
                if count > longest:
                    longest = count 
            else:
                count = 1

        return longest       