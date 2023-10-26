'''
https://practice.geeksforgeeks.org/problems/maximum-product-of-two-numbers2730/1

Given an array Arr of size N with all elements greater than or equal to zero. Return the maximum product of two numbers possible.

Example 1:

Input: 
N = 6
Arr[] = {1, 4, 3, 6, 7, 0}  
Output: 42
Example 2:

Input: 
N = 5
Arr = {1, 100, 42, 4, 23}
Output: 4200
'''

import sys
class Solution:
    
	def maxProduct(self,arr, n):
		m1=arr[0]
		m2=-sys.maxsize
		for i in range(1,n):
		    if m1< arr[i]:
		        m2=m1
    		    m1=arr[i]
    		elif m2<arr[i] and m1>=arr[i]:
    		    m2=arr[i]
    	return m1*m2

# -------- Time and Space Complexity
'''
Time Complexity: O(n)
Due to a single iteration through the array, the time complexity is O(n).
Space complexity: O(1)
Since no additional space is required, the space complexity remains constant.
'''