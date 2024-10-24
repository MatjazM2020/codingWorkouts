select
    left_operand
    , operator
    , right_operand
    , case 
        when operator = '>' then (case when (vl.value > vr.value) then 'true' else 'false' end)
        when operator = '<' then (case when (vl.value < vr.value) then 'true' else 'false' end)
        else (case when (vl.value = vr.value) then 'true' else 'false' end)
    end value
from Expressions e
inner join Variables vl on vl.name = e.left_operand
inner join Variables vr on vr.name = e.right_operand


/*
https://leetcode.com/problems/evaluate-boolean-expression/description/?envType=study-plan-v2&envId=premium-sql-50

Table Variables:

+---------------+---------+
| Column Name   | Type    |
+---------------+---------+
| name          | varchar |
| value         | int     |
+---------------+---------+
In SQL, name is the primary key for this table.
This table contains the stored variables and their values.
 

Table Expressions:

+---------------+---------+
| Column Name   | Type    |
+---------------+---------+
| left_operand  | varchar |
| operator      | enum    |
| right_operand | varchar |
+---------------+---------+
In SQL, (left_operand, operator, right_operand) is the primary key for this table.
This table contains a boolean expression that should be evaluated.
operator is an enum that takes one of the values ('<', '>', '=')
The values of left_operand and right_operand are guaranteed to be in the Variables table.
 

Evaluate the boolean expressions in Expressions table.

Return the result table in any order.


*/