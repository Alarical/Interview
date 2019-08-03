public class Solution {
    /**
     * @param nums: An array of integers
     * @return: An integer
     */
    public int maxProduct(int[] nums) {
        // write your code here
        if (nums.length == 0){
            return 0;
        }
        if (nums.length == 1){return nums[0];}
        int n = nums.length;
        int preMin = nums[0];
        int preMax = nums[0];
        int curMin = nums[0];
        int curMax = nums[0];
        int res = nums[0];
        for (int i = 1 ; i < n ; i++){
            if(nums[i] > 0){
                curMax = Math.max(nums[i] , preMax * nums[i]);
                curMin = Math.min(nums[i] , preMin * nums[i]);
            }
            else {
                curMax = Math.max(nums[i] , preMin * nums[i]);
                curMin = Math.min(nums[i] , preMax * nums[i]);
            }
            
            res = Math.max(res , curMax );
            preMax = curMax;
            preMin = curMin;
        }
        return res;
    }
}