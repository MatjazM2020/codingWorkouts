from typing import List


class Solution:
    def sampleStats(self, count: List[int]) -> List[float]:
        n = len(count)
        c = 0
        min, max, mean, median, mode = 0, 0, 0, 0, 0
        for i in range(n):
            if count[i] > 0:
                min = i
                break
        for i in range(n-1, -1, -1):
            if count[i] > 0:
                max = i
                break

        sum = 0
        totalNumber = 0
        mx = 0
        for i in range(n):
            sum += i*count[i]
            totalNumber += count[i]

            if count[i] > 0:
                if count[i] > mx:
                    mx = count[i]
                    mode = i
        mean = sum/totalNumber

        mid1, mid2 = totalNumber // 2, totalNumber // 2 + 1

        cm, m1, m2 = 0, None, None
        for i, cnt in enumerate(count):
            cm += cnt
            if m1 is None and cm >= mid1: 
                m1 = i
            if m2 is None and cm >= mid2:  
                m2 = i

        median = m2 if totalNumber % 2 == 1 else (m1 + m2) / 2


        return [min, max, mean, median, mode]
    




'''
https://leetcode.com/problems/statistics-from-a-large-sample/description/

You are given a large sample of integers in the range [0, 255]. Since the sample is so large, it is represented by an array 
count where count[k] is the number of times that k appears in the sample.

Calculate the following statistics:

minimum: The minimum element in the sample.
maximum: The maximum element in the sample.
mean: The average of the sample, calculated as the total sum of all elements divided by the total number of elements.
median:
If the sample has an odd number of elements, then the median is the middle element once the sample is sorted.
If the sample has an even number of elements, then the median is the average of the two middle elements once the sample is sorted.
mode: The number that appears the most in the sample. It is guaranteed to be unique.
Return the statistics of the sample as an array of floating-point numbers [minimum, maximum, mean, median, mode]. Answers within 10-5 of
the actual answer will be accepted.

'''