select 
    user_id
from texts t
inner join emails e using(email_id)
where date(action_date - interval 1 day) = date(signup_date)
and signup_action = 'Verified'
order by user_id asc



/*
https://leetcode.com/problems/second-day-verification/description/

Table: emails

+-------------+----------+
| Column Name | Type     | 
+-------------+----------+
| email_id    | int      |
| user_id     | int      |
| signup_date | datetime |
+-------------+----------+
(email_id, user_id) is the primary key (combination of columns with unique values) for this table.
Each row of this table contains the email ID, user ID, and signup date.
Table: texts

+---------------+----------+
| Column Name   | Type     | 
+---------------+----------+
| text_id       | int      |
| email_id      | int      |
| signup_action | enum     |
| action_date   | datetime |
+---------------+----------+
(text_id, email_id) is the primary key (combination of columns with unique values) for this table. 
signup_action is an enum type of ('Verified', 'Not Verified'). 
Each row of this table contains the text ID, email ID, signup action, and action date.
Write a Solution to find the user IDs of those who verified their sign-up on the second day.

Return the result table ordered by user_id in ascending order.

The result format is in the following example.

 

Example:

Input:

emails table:

+----------+---------+---------------------+
| email_id | user_id | signup_date         |
+----------+---------+---------------------+
| 125      | 7771    | 2022-06-14 09:30:00|
| 433      | 1052    | 2022-07-09 08:15:00|
| 234      | 7005    | 2022-08-20 10:00:00|
+----------+---------+---------------------+
texts table:

+---------+----------+--------------+---------------------+
| text_id | email_id | signup_action| action_date         |
+---------+----------+--------------+---------------------+
| 1       | 125      | Verified     | 2022-06-15 08:30:00|
| 2       | 433      | Not Verified | 2022-07-10 10:45:00|
| 4       | 234      | Verified     | 2022-08-21 09:30:00|
+---------+----------+--------------+---------------------+
    
Output:

+---------+
| user_id |
+---------+
| 7005    |
| 7771    |
+---------+
Explanation:

User with user_id 7005 and email_id 234 signed up on 2022-08-20 10:00:00 and verified on second day of the signup.
User with user_id 7771 and email_id 125 signed up on 2022-06-14 09:30:00 and verified on second day of the signup.

*/