with categories as (
    select 'Low Salary' as category 
    union 
    select 'Average Salary' as category 
    union 
    select 'High Salary' as category 
)

select 
categories.category,
coalesce(accounts_count,0) as accounts_count
from
(select
category, 
count(*) as accounts_count
from
(select 
case 
    when income < 20000 
    then "Low Salary"
    when income <= 50000
    then "Average Salary"
    else "High Salary"
end as category
from 
Accounts) as w 
group by category) as q
right join
categories
on categories.category = q.category







/*
problem: https://leetcode.com/problems/count-salary-categories/description/?envType=study-plan-v2&envId=top-sql-50


Table: Accounts
+-------------+------+
| Column Name | Type |
+-------------+------+
| account_id  | int  |
| income      | int  |
+-------------+------+
account_id is the primary key (column with unique values) for this table.
Each row contains information about the monthly income for one bank account.
 
Write a solution to calculate the number of bank accounts for each salary category. The salary categories are:

"Low Salary": All the salaries strictly less than $20000.
"Average Salary": All the salaries in the inclusive range [$20000, $50000].
"High Salary": All the salaries strictly greater than $50000.
The result table must contain all three categories. If there are no accounts in a category, return 0.
Return the result table in any order.

*/