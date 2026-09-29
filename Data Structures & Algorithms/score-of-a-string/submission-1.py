class Solution:
    def scoreOfString(self, s: str) -> int:
        

        #The score of a string is defined as the sum of the absolute difference between the ASCII values of adjacent characters.
        ans = 0 
        for i in range(len(s) - 1):
            ans += abs(ord(s[i]) - ord(s[i+1]))
        return ans
