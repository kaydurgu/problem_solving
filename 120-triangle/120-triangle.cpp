class Solution {
public:
    int minimumTotal(vector<vector<int>>& triangle) {
        for (int i = 1 ;i < triangle.size() ; i++){
            for (int j = 0 ;j < triangle[i].size() ; j++){
               if (j - 1 < 0)
                   triangle[i][j] = triangle[i][j] + triangle[i - 1][j];
               else if (j == triangle[i].size() - 1)
                   triangle[i][j] = triangle[i][j] + triangle[i - 1][j - 1]; 
               else
                    triangle[i][j] = min(triangle[i][j] + triangle[i - 1][j], triangle[i][j] + triangle[i - 1][j - 1]);
           }
        }
        int  mn = 1e5 + 9;
        for (int j = 0 ;j < triangle[triangle.size()-1].size() ; j++){
                mn = min(triangle[triangle.size()-1][j] , mn);
        }   
        return mn;
    }
};