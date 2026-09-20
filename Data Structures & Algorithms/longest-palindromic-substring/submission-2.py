class Solution:
    def longestPalindrome(self, s: str) -> str:
    
    # Given a string s, return the longest substring of s that is a palindrome.

        res = ""
        currlength = 0
        #we can use the sliding window algorithm to determine if we have a palindrome or not.
    
        # odd case
        for i in range(len(s)):
            
            L, R = i , i
            #odd case   
            while L >= 0 and R < len(s) and s[L] == s[R]:
                if (R - L + 1) > currlength:
                    res = s[L:R+1]
                    currlength = R - L + 1 
                L -= 1
                R += 1

            #even case

            L, R = i, i + 1
            while L >= 0 and R < len(s) and s[L] == s[R]:
                if (R - L + 1) > currlength:
                    res = s[L:R+1]
                    currlength = R - L + 1 
                L -= 1
                R += 1
        return res

                   