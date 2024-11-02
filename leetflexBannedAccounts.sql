select 
    distinct l.account_id
from LogInfo l
inner join LogInfo li on 
(li.login <= l.logout) and (li.logout >= l.login) and l.ip_address != li.ip_address and li.account_id = l.account_id






/*
https://leetcode.com/problems/leetflex-banned-accounts/description/?envType=study-plan-v2&envId=premium-sql-50

Table: LogInfo

+-------------+----------+
| Column Name | Type     |
+-------------+----------+
| account_id  | int      |
| ip_address  | int      |
| login       | datetime |
| logout      | datetime |
+-------------+----------+
This table may contain duplicate rows.
The table contains information about the login and logout dates of Leetflex accounts. It also contains the IP address from which the account was logged in and out.
It is guaranteed that the logout time is after the login time.
 

Write a solution to find the account_id of the accounts that should be banned from Leetflex. An account should be banned if it was logged in at some moment from two different IP addresses.

Return the result table in any order.
*/