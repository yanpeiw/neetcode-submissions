class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
    
    # We can create a HashMap that maps our keys: CharCount to our value: list of anagrams.
        res = defaultdict(list)
        
        # looping through s strings in list strs.
        for s in strs:
            # initializing count at each char, 24 for each lower cased letters.
            count = [0] * 26
            
            # looping through each char c in s, and counting at each char position 

            # we want to map letter "a" to index 0, "b" to index 1, etc.
            for c in s:
                # using ASCII letter table to normalize our indexes 
                count[ord(c) - ord("a")] += 1

            res[tuple(count)].append(s)


        return list(res.values())