func hIndex(citations []int) int {
    n := len(citations)
    l := 0
    r := n-1
    c := 0
    for l <= r{
        c = l + (r - l)/2
        if citations[c] > n - c{
            r = c - 1
        }else if citations[c] < n - c{
            l = c + 1
        }else{
            return n - c
        }
    }
    return n - l
}




/*
https://leetcode.com/problems/h-index-ii/?envType=study-plan-v2&envId=binary-search

Given an array of integers citations where citations[i] is the number of citations a researcher received for their ith paper 
and citations is sorted in ascending order, return the researcher's h-index.

According to the definition of h-index on Wikipedia: The h-index is defined as the maximum value of h such that the given 
researcher has published at least h papers that have each been cited at least h times.

You must write an algorithm that runs in logarithmic time.
*/
