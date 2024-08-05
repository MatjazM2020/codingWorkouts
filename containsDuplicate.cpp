using namespace std;
#include <vector>
#include <set>

class Solution {
public:
    bool containsDuplicate(vector<int>& nums) {
        set<int> seen;
        int n = nums.size();

        for(int elt: nums){
            if(seen.find(elt) != seen.end()){
                return true;
            }
            seen.insert(elt);
        }
        return false;
    }
};

int main(){
    
}
/*
https://leetcode.com/problems/contains-duplicate/description/

Given an integer array nums, return true if any value appears at least twice in the array,
 and return false if every element is distinct.
*/