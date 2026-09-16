class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        
    #Input: nums = [9,1,4,2,3,3,7] 

    #We can solve this by using DP, by iterating backwards from the back of the array.
    
    # Explanation: The longest subsequence starting at the last element will always be 1, if the subsequent element is less than the proceeding element, we can add 1 to the element's index, iterating through this, we can find the longest subsequence.
    
    # every value will be at 
        Lis = [1]*len(nums)

        for i in range(len(nums) - 1, -1, -1):
            for j in range((i+1), len(nums)):
                if nums[i] < nums[j]:
                    Lis[i] = max(Lis[i], Lis[j] + 1)
        return max(Lis)
        


        