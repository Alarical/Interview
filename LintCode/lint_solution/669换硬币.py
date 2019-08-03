class Solution:
    """
    @param coins: a list of integer
    @param amount: a total amount of money amount
    @return: the fewest number of coins that you need to make up
    """
    def coinChange(self, coins, amount):
        # write your code here
        import sys
        MAX_VALUE = sys.maxsize
        dp = [MAX_VALUE for i in range(amount+1)]
        dp[0] = 0
        for i in range(1,amount+1):
            for coin in coins:
                if i-coin < 0:
                    continue
                dp[i] = min(dp[i] , dp[i-coin]+1)
        if dp[amount] == MAX_VALUE:
            return -1
        return dp[amount]