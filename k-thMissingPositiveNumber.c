int findKthPositive(int* arr, int arrSize, int k) {
    int l = 0;
    int r = arrSize-1;
    int c = 0;

    while(l < r){
        c = l + (r-l)/2;
        if(arr[c]-c-1 < k){
            l = c+1;
        }else{
            r = c;
        }
    }
    
    int missing_before_l = arr[l] - l - 1;
    if(missing_before_l >= k){
       return arr[l] - (missing_before_l-k+1);
    }
    return arr[l] + (k - missing_before_l);
}


/*
https://leetcode.com/problems/kth-missing-positive-number/description/?envType=study-plan-v2&envId=binary-search
Given an array arr of positive integers sorted in a strictly increasing order, and an integer k.

Return the kth positive integer that is missing from this array.

*/