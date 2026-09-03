class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
    
        res = []
        nums.sort()
        
        for i, x in enumerate(nums):
            #check if it's not the first element and check if it is equal to the prior element
            if i > 0 and x == nums[i - 1]: 
                continue

            L, R = i + 1 , len(nums) - 1

            while L < R:

                sum = x + nums[L] + nums[R]

                if sum > 0:
                    R -= 1
                elif sum < 0:
                    L += 1
                else:
                    res.append([x, nums[L], nums[R]])
                    L += 1
                    while L < R and nums[L] == nums[L - 1] :
                         L += 1
        return res
                
                
                    


    
        