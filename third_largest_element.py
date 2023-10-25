'''
https://practice.geeksforgeeks.org/problems/third-largest-element/1?utm_source=geeksforgeeks&utm_medium=article_practice_tab&utm_campaign=article_practice_tab

Given an array of distinct elements. Find the third largest element in it.

Example 1:

Input:
N = 5
A[] = {2,4,1,3,5}
Output: 3
Example 2:

Example 2:
Input:
N = 2
A[] = {10,2}
Output: -1
'''

import sys
class Solution:
    
    def thirdLargest(self,a, n):
        if n<3:
            return
        m1=a[0]
        m2=m3=-sys.maxsize
        for i in range(1,len(a)):
            if a[i]>m1:
                m3=m2
                m2=m1
                m1=a[i]

            if a[i]>m2 and a[i]<m1:
                m3=m2
                m2=a[i]
                
            if a[i]>m3 and a[i]<m2 and a[i]<m1:
                m3=a[i]
        return m3
    
# -------- Time and Space Complexity
'''
Time Complexity: O(n)
Due to a single iteration through the array, the time complexity is O(n).
Space complexity: O(1)
Since no additional space is required, the space complexity remains constant.
'''