SELECT 
    id,
    MAX(CASE WHEN month = 'Jan' THEN revenue ELSE NULL END) AS Jan_Revenue,
    MAX(CASE WHEN month = 'Feb' THEN revenue ELSE NULL END) AS Feb_Revenue,
    MAX(CASE WHEN month = 'Mar' THEN revenue ELSE NULL END) AS Mar_Revenue,
    MAX(CASE WHEN month = 'Apr' THEN revenue ELSE NULL END) AS Apr_Revenue,
    MAX(CASE WHEN month = 'May' THEN revenue ELSE NULL END) AS May_Revenue,
    MAX(CASE WHEN month = 'Jun' THEN revenue ELSE NULL END) AS Jun_Revenue,
    MAX(CASE WHEN month = 'Jul' THEN revenue ELSE NULL END) AS Jul_Revenue,
    MAX(CASE WHEN month = 'Aug' THEN revenue ELSE NULL END) AS Aug_Revenue,
    MAX(CASE WHEN month = 'Sep' THEN revenue ELSE NULL END) AS Sep_Revenue,
    MAX(CASE WHEN month = 'Oct' THEN revenue ELSE NULL END) AS Oct_Revenue,
    MAX(CASE WHEN month = 'Nov' THEN revenue ELSE NULL END) AS Nov_Revenue,
    MAX(CASE WHEN month = 'Dec' THEN revenue ELSE NULL END) AS Dec_Revenue
FROM Department
GROUP BY id;



/*
https://leetcode.com/problems/reformat-department-table/description/

Table: Department

+-------------+---------+
| Column Name | Type    |
+-------------+---------+
| id          | int     |
| revenue     | int     |
| month       | varchar |
+-------------+---------+
In SQL,(id, month) is the primary key of this table.
The table has information about the revenue of each department per month.
The month has values in ["Jan","Feb","Mar","Apr","May","Jun","Jul","Aug","Sep","Oct","Nov","Dec"].
 

Reformat the table such that there is a department id column and a revenue column for each month.

Return the result table in any order.

The result format is in the following example.
*/
