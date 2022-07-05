class Solution {
public:
    int longestConsecutive(vector<int>& nums) {
        sort(nums.begin(),nums.end());
        int cnt = 1,mx = 0;
        if (nums.size() == 0)
            return 0;
        for (int i = 0 ;i < nums.size() - 1; i++){
            if (nums[i] + 1 == nums[i + 1] )
                cnt++;
            else if (nums[i]!=nums[i+1]){
                mx = max(cnt , mx);
                cnt = 1;
             }
        }
        return max(mx,cnt);
    }
};