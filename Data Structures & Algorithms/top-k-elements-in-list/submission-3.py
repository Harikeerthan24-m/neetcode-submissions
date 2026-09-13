import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
    # brute force 
    # idea 
      # find the freq values 
      # get those values per keys 
      # sort it in descending order 
      # slice upto k 

    # CODE:  
      freq = {}

      # find the freq count 
      for i in nums:
          freq[i] = freq.get(i,0)+1
      
      # sort key by values 
      # sort makes the dict into list of tuple pairs
      ans = sorted(freq.items(),key=lambda x:x[1],reverse=True)
      
      # get the ans by get through the list 
      # access tuple by use list comprehension 
      return [x[0] for x in ans[:k]]
            
        