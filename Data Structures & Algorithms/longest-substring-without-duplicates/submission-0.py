class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        
        charSet = set()
        res = 0
        L = 0 
        
        #using sliding window algo to determine the longest subsequence without duplicates

        
        for r in range(len(s)):
            #while s[r] exists inside of our set, we increment the left ptr 
            while s[r] in charSet:
                charSet.remove(s[L])
                L += 1 
            charSet.add(s[r])
            res = max(res, r - L + 1 )
        return res
            


        
        
        