prices = [7,1,5,3,6,4]
class Solution:     
    """Solve stock profit calculations."""

    def max_profit(self, prices: list[int]) -> int:
        # min_price = float('inf')
        # max_price = 0
        # for price in prices:
        #     min_price = min(min_price, price)
        #     profit = price - min_price
        #     max_price = max(max_price, profit)
        # using kadane algorithm
        max_price = 0
        current_profit = 0
        for i in range(1, len(prices)):
            diff = prices[i] - prices[i-1]
            current_profit = max(0, current_profit + diff)
            max_price = max(max_price, current_profit)

        return max_price
    
Solution = Solution() # type: ignore
result = Solution.max_profit(prices) # type: ignore
print(result)