 select DATE_FORMAT(day, '%W, %M %e, %Y') day
 from Days


/*
https://leetcode.com/problems/convert-date-format/

Table: Days

+-------------+------+
| Column Name | Type |
+-------------+------+
| day         | date |
+-------------+------+
day is the column with unique values for this table.
 

Write a solution to convert each date in Days into a string formatted as "day_name, month_name day, year".

Return the result table in any order.

The result format is in the following example.

 

Example 1:

Input: 
Days table:
+------------+
| day        |
+------------+
| 2022-04-12 |
| 2021-08-09 |
| 2020-06-26 |
+------------+
Output: 
+-------------------------+
| day                     |
+-------------------------+
| Tuesday, April 12, 2022 |
| Monday, August 9, 2021  |
| Friday, June 26, 2020   |
+-------------------------+
Explanation: Please note that the output is case-sensitive.

*/