class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # track the count of consecutive numbers
        count = 1
        longest = 1

        # sort the array first
        sorted_nums = sorted(nums)

        if len(nums) <= 0:
            return 0
        
        # use for loop 
        for i in range(len(sorted_nums)):
            # check duplicates
            if i < 1:
                continue
            elif sorted_nums[i-1] == sorted_nums[i]:
                continue
            elif sorted_nums[i-1] + 1 == sorted_nums[i]:
                count += 1
                if count > longest:
                    longest = count 
            else:
                count = 1

        return longest
        