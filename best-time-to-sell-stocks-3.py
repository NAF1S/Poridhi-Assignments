

class Solution:

    def maxProfit(self,prices: list[int]) -> int:
        n = len(prices)
        dp = {}

        def f(i: int, buy: int, rem: int) -> int:
            if i == n:
                return 0
            if (i, buy, rem) in dp:
                return dp[(i, buy, rem)]
            if buy == 1:
                if rem == 0:
                    return 0
                b = -prices[i] + f(i + 1, 0, rem)
                skip = f(i + 1, 1, rem)
                dp[(i, buy, rem)] = max(b, skip)
                return dp[(i, buy, rem)]
            else:
                sell = prices[i] + f(i + 1, 1, rem - 1)
                skip = f(i + 1, 0, rem)
                dp[(i, buy, rem)] = max(sell, skip)
                return dp[(i, buy, rem)]

        return f(0, 1, 2)


