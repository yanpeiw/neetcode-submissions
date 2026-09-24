class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:

        # return true if string 2 there is a substring permutation in string 1 

        # substring must be in sequential order

        # iterate through str s2 

        if len(s1) > len(s2):
            return False
        
        need = {}
        window = {}
        
        for char in s1:
            need[char] = need.get(char, 0) + 1
        
        for char in s2[:len(s1)]:
            window[char] = window.get(char, 0) + 1 
        
        if window == need: 
            return True
        
        L = 0

        for r in range(len(s1), len(s2)):
            entering = s2[r]
            window[entering] = window.get(entering, 0) + 1 

            leaving = s2[L]
            window[leaving] -= 1

            if window[leaving] == 0:
                del window[leaving]
            
            L += 1

            if window == need:
                return True

        return False


        
        

        
        
        
        

        

        