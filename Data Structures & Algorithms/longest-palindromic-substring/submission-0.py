class Solution:
    def longestPalindrome(self, s: str) -> str:
    
    # Given a string s, return the longest substring of s that is a palindrome.

        res = ""
        resLength = 0 

        for i in range(len(s)):

            L, R = i,i 
            #if the length of the sequence is odd
            while L >= 0 and R < len(s) and s[L] == s[R]:
                if (R - L + 1) > resLength:
                    res = s[L:R+1]
                    resLength = (R - L) + 1
                L -= 1
                R += 1

            #if the length of the sequence is even
            
            L, R = i, i + 1
            while L >= 0 and R < len(s) and s[L] == s[R]:
                if (R - L + 1) > resLength:
                    res = s[L:R+1]
                    resLength = (R - L) + 1
                L -= 1
                R += 1   
        return res
                   