# Write your MySQL query statement below

select
    transaction_date
    , sum(case when amount % 2 != 0 then amount else 0 end) odd_sum
    , sum(case when amount % 2 = 0 then amount else 0 end) even_sum
from transactions
group by transaction_date 
order by transaction_date asc


/*
https://leetcode.com/problems/odd-and-even-transactions/description/

Table: transactions

+------------------+------+
| Column Name      | Type | 
+------------------+------+
| transaction_id   | int  |
| amount           | int  |
| transaction_date | date |
+------------------+------+
The transactions_id column uniquely identifies each row in this table.
Each row of this table contains the transaction id, amount and transaction date.
Write a solution to find the sum of amounts for odd and even transactions for each day.
 If there are no odd or even transactions for a specific date, display as 0.

Return the result table ordered by transaction_date in ascending order.

The result format is in the following example.
*/