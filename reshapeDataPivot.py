import pandas as pd
def pivotTable(weather: pd.DataFrame) -> pd.DataFrame:
    pivoted = weather.pivot_table(index='month', columns='city', values='temperature')
    return pivoted




'''
https://leetcode.com/problems/reshape-data-pivot/description/

DataFrame weather
+-------------+--------+
| Column Name | Type   |
+-------------+--------+
| city        | object |
| month       | object |
| temperature | int    |
+-------------+--------+
Write a solution to pivot the data so that each row represents temperatures for a specific month, and each city is a separate column.

The result format is in the following example.

'''