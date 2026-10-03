class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # brute force 
        # for each substr , gonna find out the replace count if that count is <=k then update the long 
        # long = 0 
        # n = len(s)

        # # for each substr 
        # for i in range(n):
        #     freq = {}
        #     for j in range(i,n):
        #         freq[s[j]] = freq.get(s[j],0) + 1
        #         sub_len = j - i + 1
        #         replace_count = sub_len - max(freq.values())
        #         if replace_count <= k:
        #             long = max(long,sub_len)
        # return long 

        # optimal solution 
        # what is repetitve : overlapping of the same substrings 
        # what is missing : not tracking the substring which has already replace count align with k , instead starting it from scratch 
        # ds : sliding window 
        # how : maintain a single substring under the window , and find the replace count if the count is <= k then window is invalid so shrink it from left 
        long = 0 
        n = len(s)
        left = 0 
        freq = {}
        for right in range(n):
            freq[s[right]] = freq.get(s[right],0) + 1
            window_len = right - left + 1
            # check the replace count 
            replace_count = window_len - max(freq.values())
            # invalid window check 
            while replace_count > k:
                # remove the count of the char 
                freq[s[left]] -= 1
                left+=1
                print(left)
                # update the replace check else it wont get of from the while loop 
                window_len = right - left + 1
                # check the replace count 
                replace_count = window_len - max(freq.values())
            # update the long 
            long = max(long,window_len)
        return long




        