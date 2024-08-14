int arrangeCoins(int n) {
    int l = 1;
    int r = n;
    int c = n/2;
    long int sum = 0;
    while(l <= r){
        c = l + (r - l)/2;
        sum = (long long) c*(c+1)/2;
        if(sum > n){
            r = c - 1;
        }else if(sum < n){
            l = c + 1;
        }else{ 
            return c;
        }
    }
    return l - 1;
}


/*
https://leetcode.com/problems/arranging-coins/description/?envType=study-plan-v2&envId=binary-search

You have n coins and you want to build a staircase with these coins. The staircase consists of k rows where
 the ith row has exactly i coins. The last row of the staircase may be incomplete.

Given the integer n, return the number of complete rows of the staircase you will build.



*/