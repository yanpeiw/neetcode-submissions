class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        # Given an array of integers nums and an integer target, return the indices i and j such that nums[i] + nums[j] == target and i != j.

        #use hashmap, python dict 

        sumMap= {}

        for i, v in enumerate(nums):

            #calculate the difference between the target value and v, check if complement exists
            diff = target - v 
            if diff in sumMap:
                return [sumMap[diff], i]
                
            sumMap[v] = i




            


            
            
            
            
        
            
            
            