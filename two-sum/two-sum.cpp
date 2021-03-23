#include <bits/stdc++.h>


class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        
        unordered_map<int, int> map;
        vector<int> ans;
        
        for(int i=0; i < nums.size(); i++){
            int comp = target - nums[i];
            if( map.count(comp) ){
                ans.push_back(map[comp]);
                ans.push_back(i);
                return ans;
            }
            map[nums[i]] = i;
        }
        return ans;
    }
};