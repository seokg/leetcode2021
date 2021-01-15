class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        profit = 0
        for i in range(1, len(prices)):
            if prices[i] > prices[i-1]:
                profit += prices[i] - prices[i-1]
                
        return profit

#         min_price = None
#         profit = 0
#         for i in range(len(prices)):
#             if i != 0:
#                 if prices[i] < prices[i-1]:
#                     print(f'set min price {prices[i]} < {prices[i-1]}')
#                     min_price = prices[i]
#                 else:
#                     print(f'profit at {i}' )
#                     profit += prices[i] - min_price
#                     min_price = prices[i]
#             else:
#                 min_price = prices[0]
                
#         return profit
        
