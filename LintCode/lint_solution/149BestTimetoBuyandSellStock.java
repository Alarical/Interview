public class Solution {
    /**
     * @param prices: Given an integer array
     * @return: Maximum profit
     */
    public int maxProfit(int[] prices) {
        // write your code here
        int min_Value = Integer.MAX_VALUE;
        int res = 0;
        for (int i = 0 ; i < prices.length ; i++){
            if (prices[i] <= min_Value)
                min_Value = prices[i];
            res = Math.max(res , prices[i] - min_Value);
        }
        return res;
    }
}