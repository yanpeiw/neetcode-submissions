class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
    
    # element must be exactly 1 greater than the previous element

        longest = 0 

        numSet = set(nums)

        for n in nums:
            
        # checking the start of the sequence
            if n - 1 not in numSet:

                length = 1
                
                # We check if n + 1 exists in our numset,
                while(n + length) in numSet:
                    length += 1

                longest = max(longest,length)
        return longest   
                

                
                
                
        

