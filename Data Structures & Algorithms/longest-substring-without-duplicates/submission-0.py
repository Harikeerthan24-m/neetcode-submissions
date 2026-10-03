class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # brute force 
        # check for each sub str count without duplication , update the count to long 
        # long = 0 
        # n = len(s)

        # # check every substr
        # for i in range(n):
        #     dup_check = set() # to track the dup
        #     for j in range(i,n):
        #         # check the dup in set 
        #         if s[j] in dup_check:
        #             break 
        #         # add it to set if not 
        #         dup_check.add(s[j])
        #     count = len(dup_check)
        #     long = max(long,count)
        # return long 

        # optimal solution 
        # what is repetitve : overlapping of the same substrings 
        # what is missing : tracking the value which already have long substring wihtout duplicates 
        # ds : sliding window 
        # how : using (variable) sliding window to maintain single substr window , if duplicates which makes the window invalid shirnk it from the left 
        long = 0 
        n = len(s)
        left = 0 
        dup_check = set()
        for right in range(n):
            # if we get dup window will invalid so 
            while s[right] in dup_check:
                # remove the left vale 
                dup_check.remove(s[left])
                left+=1
            # else add it 
            dup_check.add(s[right])
            # check the count 
            count = len(dup_check)
            # update the long 
            long = max(long,count)
        return long



   