class Solution:
    def validPalindrome(self, s: str) -> bool:
        
        if s == s[::-1]:
            return True

        L, R = 0, len(s) - 1 

        while L < R:
            
            if s[L] != s[R]:
                skipL = s[L + 1 : R + 1]
                skipR = s[L : R]
                return skipL == skipL[::-1] or skipR == skipR[::-1]
            L += 1 
            R -= 1
        return True

                


        
