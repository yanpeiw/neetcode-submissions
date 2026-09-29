class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        # alternately merge the 2 arrays, word1 and word2, starting with word1
        newStr= ""
        
        for i, j in zip(word1, word2):
            newStr += i + j
            
        minlen = min(len(word1),len(word2))  
        newStr += word1[minlen:] + word2[minlen:]
        
        return newStr

            
            
        


        