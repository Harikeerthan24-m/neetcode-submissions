class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded_word = "".join([str(len(i)) + "#" + i for i in strs])
        return encoded_word
    
        
    def decode(self, encoded_word: str) -> List[str]:
        # pseudocode
        # need to find the number / extrsct it 
        # extract the word from it 
        # append it to that list 
        
        decode_words = []
        i = 0 
        track = 0 
        num = 0 

        while i < len(encoded_word):

            # 1. get the number 
            if encoded_word[i] == "#":
                num = int(encoded_word[track:i])
            
                # 2.get the word 
                start = i+1 #word start after the #
                end = num + start # word ended + next str due to the exclusiveness 

                word = encoded_word[start:end]

                # append to the list
                decode_words.append(word)

                track = end # update the track to extract num
                i = end # update the i to move to the next end directly
            else:
                i+=1

        return decode_words


        


            

