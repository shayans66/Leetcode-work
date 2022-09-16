class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        cur,sofar = 0, 0
        for i in range(1, len(prices)):
            cur = max(0, cur + prices[i] - prices[i-1])
            sofar = max(cur, sofar)
        return sofar