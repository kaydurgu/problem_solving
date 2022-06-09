class Solution {
public:
    vector<int> twoSum(vector<int>& numbers, int target) {
        int left = 0 ;
          vector<int> ans;
        int right = numbers.size() - 1;
        while(left < right){
            if (numbers[left] + numbers[right] == target){
                ans.push_back(left + 1);
                ans.push_back(right + 1);
                return ans;
            }
            if (numbers[left] + numbers[right] < target)
                left++;
            else
                right --;
        }
        return ans;
    }
};