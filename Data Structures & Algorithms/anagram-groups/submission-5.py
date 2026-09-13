class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

    # brute force solution
    # pseudocode
        # for each strs 
        # for each with next strs next to i 
        # if sorted of i == sorted j 
        # add those as a list 
        # track which strs were added so to ignore the duplicates 
        
    # code:
    #     n = len(strs)
    #     anagram_list = [] 
    #     visited = set() # track the strs which included
    #     # first value
    #     for i in range(n):
    #         if strs[i] in visited:
    #             continue
            
    #         group = [strs[i]]
    #         visited.add(strs[i])

    #         for j in range(i+1,n):
    #             if strs[j] not in visited:
    #                 if ''.join(sorted(strs[i])) == ''.join(sorted(strs[j])):
    #                     group.append(strs[j])
    #                     visited.add(strs[j])

    #         anagram_list.append(group)  
    #     return anagram_list

    # optimal solution 
    # pseudocode 
      # use the char freq for each word 
      # if a word can match that means add it to those list

    # code 
        freq = {}
    # loop to each strs 
        for s in strs:
            # find the char freq
            char_freq = [0]*26
            for word in s:
                idx = ord(word) - ord('a')
                char_freq[idx]+=1
    
            unmutable_key = tuple(char_freq)
            # update the char freq is in freq
            if unmutable_key not in freq:
                freq[unmutable_key] = [s]
            else:
                freq[unmutable_key].append(s)

        return list(freq.values())

        




    