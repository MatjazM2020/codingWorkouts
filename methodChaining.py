import pandas as pd

def findHeavyAnimals(animals: pd.DataFrame) -> pd.DataFrame:
    filtered = animals[animals['weight'] > 100]
    srtd = filtered.sort_values(by='weight', ascending=False)
    return srtd[['name']]



'''
https://leetcode.com/problems/method-chaining/submissions/1397404106/

DataFrame animals
+-------------+--------+
| Column Name | Type   |
+-------------+--------+
| name        | object |
| species     | object |
| age         | int    |
| weight      | int    |
+-------------+--------+
Write a solution to list the names of animals that weigh strictly more than 100 kilograms.

Return the animals sorted by weight in descending order.

The result format is in the following example.

'''