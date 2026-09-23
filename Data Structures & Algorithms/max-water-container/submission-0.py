class Solution:
    def maxArea(self, heights: List[int]) -> int:
        
        # We want to maximize the heights

        # start with two pointers starting at index 0 and len(List) - 1

        L, R = 0, len(heights) - 1
        
        maxArea = 0 

        while L < R:

            area = (R - L) * min(heights[L], heights[R])
            maxArea = max(maxArea, area)

            if heights[L] < heights[R]:
                L += 1 
            elif heights[L] > heights[R]:
                R -= 1 
            else: 
                L += 1 
                R -= 1
            
        return maxArea
                
                

            
        