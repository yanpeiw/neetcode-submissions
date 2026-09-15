class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        # Input: nums = [1,2,4,6]
        # Given an integer array nums, return an array output where output[i] is the product of all the elements of nums except nums[i].
        n = len(nums)

        #setting 3 arrays, prefix, suffix, and result arrays
        
        pref = [0]* n
        suff = [0]* n
        res = [0]* n

        #example nums arr: [1,2,3,4]
        
        #prev array is everything before the i-th index
        pref[0] = suff[n-1] = 1 
        for i in range(1,n):
            pref[i] = nums[i-1] * pref[i-1]
        for i in range(n - 2, -1, -1 ):
            suff[i] = nums[i+1] * suff[i+1]
        for i in range(n):
            res[i] = pref[i] * suff[i]
        

        return res
             
