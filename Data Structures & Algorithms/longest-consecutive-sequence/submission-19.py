class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        count = 1
        longest = 1 
        # sort the values
        sorted_nums = sorted(nums)
        sorted_len = len(sorted_nums) 

        # 0 check 
        if sorted_len == 0:
            return 0 

        # loop 
        for i in range(sorted_len):
            # previous value check 
            if i < 1:
                continue
            # duplicate check 
            elif sorted_nums[i-1] == sorted_nums[i]:
                continue
            # core check 
            elif sorted_nums[i-1] + 1 == sorted_nums[i]:
                count += 1
                if count > longest:
                    longest = count 
            else:
                count = 1

        return longest       