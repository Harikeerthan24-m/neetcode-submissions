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
    #   freq = {}

    #   # find the freq count 
    #   for i in nums:
    #       freq[i] = freq.get(i,0)+1
      
    #   # sort key by values 
    #   # sort makes the dict into list of tuple pairs
    #   ans = sorted(freq.items(),key=lambda x:x[1],reverse=True)
      
    #   # get the ans by get through the list 
    #   # access tuple by use list comprehension 
    #   return [x[0] for x in ans[:k]]

    # optimal 
    # pseudocode 
      # take the freq count 
      # use the bucket sort to sort the elements by the freq as idx 
      # extract the values upto the k limit 
      
    # code: 
        freq = {}
        # frequency count 
        for i in nums:
          freq[i] = freq.get(i,0) + 1

        # buckets sorting
        buckets = [[] for _ in range(len(nums)+1)]

        # place the elements based on freq idx 
        for key , value in freq.items():
            buckets[value].append(key)

        # extract the keys upto k limit 
        # get from right cause need max 
        results = [] 
        for key in range(len(buckets)-1,-1,-1):
          if buckets[key] != []:
              results.extend(buckets[key])

          if len(results) == k:
              break 

        return results



            
        