class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashmap = {}
        for i in strs:
            ch_freq = [0]*26
            for j in i:
                idx = ord(j) - ord('a')
                ch_freq[idx] += 1
            if tuple(ch_freq) in hashmap:
                hashmap[tuple(ch_freq)].append(i)
            else:
                hashmap[tuple(ch_freq)] = [i] 
        return list(hashmap.values())


            
        