int singleNonDuplicate(int* nums, int numsSize){
    int l = 0;
    int r = numsSize-1;
    int c = 0;
    while(l < r){
        c = l + (r-l)/2;
        if(c % 2 == 1){
            c -= 1;
        }
        if(nums[c] == nums[c+1]){
            l = c + 2;
        }else{
            r = c;
        }
    }
    return nums[l];
}


/*
https://leetcode.com/problems/single-element-in-a-sorted-array/description/

You are given a sorted array consisting of only integers where every element appears exactly twice, except for one element which appears exactly once.

Return the single element that appears only once.

Your solution must run in O(log n) time and O(1) space.
*/