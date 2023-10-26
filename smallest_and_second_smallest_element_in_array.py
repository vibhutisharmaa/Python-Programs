'''
https://practice.geeksforgeeks.org/problems/find-the-smallest-and-second-smallest-element-in-an-array3226/1?utm_source=geeksforgeeks&utm_medium=article_practice_tab&utm_campaign=article_practice_tab

Given an array of integers, your task is to find the smallest and second smallest element in the array. If smallest and second smallest do not exist, print -1.

Example 1:
Input :
5
2 4 3 5 6
Output :
2 3 

Example 2:
Input :
6
1 2 1 3 6 7
Output :
1 2 

'''

import sys
def minAnd2ndMin(a, n):

    if len(a)<2:
        return [-1]
    m1=a[0]
    m2=sys.maxsize
    for i in range(1, len(a)):
        if m1>a[i]:
            m2=m1
            m1=a[i]
        if m2>a[i] and m1<a[i]:
            m2=a[i]
    if m1==m2 or m2==sys.maxsize:
        return [-1]
    return m1, m2

# -------- Time and Space Complexity
'''
Time Complexity: O(n)
Due to a single iteration through the array, the time complexity is O(n).
Space complexity: O(1)
Since no additional space is required, the space complexity remains constant.
'''