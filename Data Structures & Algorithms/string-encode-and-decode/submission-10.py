class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded_word = "".join([str(len(i)) + "#" + i for i in strs])
        return encoded_word
    
        
    def decode(self, encoded_word: str) -> List[str]:
        # pseudocode
        # need to find the number / extrsct it 
        # extract the word from it 
        # append it to that list 

        decoded_words = [] 
        i = 0 
        num = 0 
        track = 0 
        while i < len(encoded_word):
            # 1. get the number
            if encoded_word[i] == "#":
                num = int(encoded_word[track:i])
                print(num)
                # 2. get the word using the num
                start = i+1
                end = start + num 

                word = encoded_word[start : end]

                decoded_words.append(word)

                track = end
                i = end
            else:
                i+=1

        return decoded_words
            



            

