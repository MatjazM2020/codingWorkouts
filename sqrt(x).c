int mySqrt(int x) {
 int l = 1; 
 int r = x; 
 long int c = 1; 
 while(l <= r){
        c = l + (r - l)/2;
        if(c*c > x){
            r = c - 1;
        }else if(c*c < x){
            l = c + 1;
        }else{
            return c;
        }
    }
    return l-1;   
}


/*
https://leetcode.com/problems/sqrtx/submissions/1354587259/?envType=study-plan-v2&envId=binary-search
Given a non-negative integer x, return the square root of x rounded down to the nearest integer. The returned integer should be non-negative as well.

You must not use any built-in exponent function or operator.

For example, do not use pow(x, 0.5) in c++ or x ** 0.5 in python.

*/