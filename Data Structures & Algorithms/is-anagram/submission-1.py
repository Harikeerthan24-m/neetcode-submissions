class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
    # brute force ------
    # pseudocode:
       # for each chars 
       # s = list()
       # if t[i] in s_list 
    # solution:
        # s_list = list(s)
        # for i in t:
        #     if i in s_list:
        #        s_list.remove(i)
        #     elif i not in s_list:
        #      return False
        # # s_list not empty means its false
        # if s_list != []:
        #     return False
        # return True
    # T.C = O(N^2) , S.C = O(N)

    # optimal ----------------
    # pseudocode
       # use the hashmap to handle the freq count of each 
       # if the values of s in t then reduced the count until 0 
       # if goes to -1 means it will be not anagrams 

    # solution :
       
       # check the str are anagrams by length 
       if len(s) != len(t):
        return False

       # take the freq count using hashmap 
       freq = {}
       for i in s:
        freq[i] = freq.get(i,0) + 1

       # check t is in freq 
       for i in t:
        if i in freq and not freq[i] == 0 :
            # reduce the count 
            freq[i] -= 1
        else:
            return False

       return True
      


        
           


        
       

        