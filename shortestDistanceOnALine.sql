select 
    min(abs(p1.x - p2.x)) shortest
from Point p1
inner join Point p2 on p1.x != p2.x



/*
https://leetcode.com/problems/shortest-distance-in-a-line/description/?envType=study-plan-v2&envId=premium-sql-50

Table: Point

+-------------+------+
| Column Name | Type |
+-------------+------+
| x           | int  |
+-------------+------+
In SQL, x is the primary key column for this table.
Each row of this table indicates the position of a point on the X-axis.
 

Find the shortest distance between any two points from the Point table.
*/