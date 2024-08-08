/** 
 * Forward declaration of guess API.
 * @param  num   your guess
 * @return 	     -1 if num is higher than the picked number
 *			      1 if num is lower than the picked number
 *               otherwise return 0
 * int guess(int num);
 */


class Solution {
public:
    int guessNumber(int n) {
        int l = 0;
        int r = n;
        int c = 0;
        int g = 0;
        while (l <= r){
            c = l + (r - l) / 2;
            g = guess(c);
            if(g == -1){
                r = c-1;
            }else if(g == 1){
                l = c+1;
            }else{
                return c;
            }
        }
        return c;
    }
};


/*
https://leetcode.com/problems/guess-number-higher-or-lower/description/?envType=study-plan-v2&envId=binary-search

We are playing the Guess Game. The game is as follows:

I pick a number from 1 to n. You have to guess which number I picked.

Every time you guess wrong, I will tell you whether the number I picked is higher or lower than your guess.

You call a pre-defined API int guess(int num), which returns three possible results:

-1: Your guess is higher than the number I picked (i.e. num > pick).
1: Your guess is lower than the number I picked (i.e. num < pick).
0: your guess is equal to the number I picked (i.e. num == pick).
Return the number that I picked.
*/