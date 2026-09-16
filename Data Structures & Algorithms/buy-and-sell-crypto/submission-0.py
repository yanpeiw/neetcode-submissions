class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        #Input: prices = [10,1,5,6,7,1]
         
        #Return the Maximum Proft: 6
        maxprofit = 0 
        L, R = 0, 1

        while R < len(prices):
            if prices[L] < prices[R]:
                profit = prices[R] - prices[L]
                maxprofit = max(maxprofit, profit)
            else:
                L = R
            R += 1
        return maxprofit
                


         