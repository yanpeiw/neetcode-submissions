class Solution:
    def mySqrt(self, x: int) -> int:
        
        L, R = 0, x

        ans = 0

        while L <= R:
            m =  L + (R-L) // 2

            if m * m < x:
                L = m + 1 
                ans = m
            elif m*m > x:
                R = m - 1

            else: 
                return m
        return ans 
        

