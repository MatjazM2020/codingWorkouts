
with x as (
    select 
    count(email) c, email
    from Person
    group by email
)

select email from x where c>1


/* https://leetcode.com/problems/duplicate-emails/description/

Table: Person

+-------------+---------+
| Column Name | Type    |
+-------------+---------+
| id          | int     |
| email       | varchar |
+-------------+---------+
id is the primary key (column with unique values) for this table.
Each row of this table contains an email. The emails will not contain uppercase letters.
Write a solution to report all the duplicate emails. Note that it's guaranteed that the email field is not NULL.

Return the result table in any order.

The result format is in the following example.
*/ 