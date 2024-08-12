bool isPerfectSquare(int num) {
    
    int l = 1;
    int r = num;
    long int c = 0; 
    while(l <= r){
        c = l + (r-l)/2;
        if(c*c>num){
            r = c - 1;
        }else if(c*c<num){
            l = c + 1;
        }else{
            return true;
        }
    }
    return false;
}


/*
https://leetcode.com/problems/valid-perfect-square/?envType=study-plan-v2&envId=binary-search

Given a positive integer num, return true if num is a perfect square or false otherwise.
A perfect square is an integer that is the square of an integer. In other words, it is the product of some integer with itself.
You must not use any built-in library function, such as sqrt.

*/