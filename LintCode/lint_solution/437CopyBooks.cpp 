class Solution {
public:
    /**
     * @param pages: an array of integers
     * @param k: An integer
     * @return: an integer
     */
    int copyBooks(vector<int> &pages, int k) {
        // write your code here
        int n = pages.size();
        int minTime = 0 , maxTime = 0;
        for (int i = 0; i < n; ++i) {
            minTime = max(minTime , pages[i]);
            maxTime += pages[i];
        }
        int left = minTime , right = maxTime;
        while(left + 1 < right){
            int mid = left+ (right -left)/2;
            if (check(pages , mid , k)){
                right = mid;
            }else{
                left = mid;
            }
        }
        if(check(pages , left , k)) {
            return left;
        }
        else {
            return right;
        }

    }
    
    bool check(vector<int> &pages, int TL, int k) {
        int sum = 0;
        int countK = 1;
        for(int i = 0 ;i < pages.size() ; i++){
            if (pages[i] > TL) return false;
            if (pages[i] + sum <= TL){
                sum += pages[i];
            } else {
                countK += 1;
                sum = pages[i];
            }
        }
        return countK <= k;
    }
};