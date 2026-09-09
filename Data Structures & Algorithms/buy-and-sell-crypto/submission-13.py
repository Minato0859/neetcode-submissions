class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # if right is greater than left, update left
        # if new profit is not greater than current_max_profit, dont update left pointer
        # always update right

        left = 0
        right = 1
        max_profit=0
        while right < len(prices):
            profit = prices[right] - prices[left]
            max_profit = max(profit, max_profit)

            if prices[right] < prices[left]:
            
                left = right
                right += 1
            else:
                right +=1

        return max_profit