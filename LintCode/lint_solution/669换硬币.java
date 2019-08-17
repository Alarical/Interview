public class Solution {
    /**
     * @param coins: a list of integer
     * @param amount: a total amount of money amount
     * @return: the fewest number of coins that you need to make up
     */
    public int coinChange(int[] coins, int amount) {
        // write your code here
        int []dp = new int[amount+1];
        dp[0] = 0;
        int n = coins.length;
        for (int i = 1 ; i <= amount ; i++) {
            dp[i] = Integer.MAX_VALUE;
            for (int j = 0 ; j < n ; j++) {
                if ( i - coins[j] >= 0 && dp[i - coins[j]] != Integer.MAX_VALUE) {
                    dp[i] = Math.min(dp[i] , dp[i - coins[j]] + 1);
                }
            }
        }
        if (dp[amount] == Integer.MAX_VALUE) 
            return -1;
        else {
            return dp[amount];
        }
    }
}