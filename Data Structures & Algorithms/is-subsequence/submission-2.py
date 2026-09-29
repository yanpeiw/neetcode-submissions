class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:

        # Return true if s is a subsequence of t

        i, j = 0, 0
        
        while i < len(s) and j < len(t):
            if s[i] == t[j]:
                i += 1
            j += 1
        # We utilize i == len(s) because this statement only returns true if our i index value for s reaches the end, indicating that we have found a subsequence.
        return i == len(s)
            
            


        
        
        