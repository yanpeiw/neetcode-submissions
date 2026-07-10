class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)!= len(t):
            return False
        #list of characters
        CountS, CountT = {},{}
        #iterate through the two strings and return the frequency of each letter
        for i in range(len(s)):
            CountS[s[i]] = 1 + CountS.get(s[i], 0)
            CountT[t[i]] = 1 + CountT.get(t[i], 0)
        return CountS == CountT
            
            
            

    