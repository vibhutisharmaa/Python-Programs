'''
https://practice.geeksforgeeks.org/problems/greater-on-right-side4305/1

You are given an array Arr of size N. Replace every element with the next greatest element (greatest element on its right side) in the array. Also, since there is no element next to the last element, replace it with -1.

Example 1:

Input:
N = 6
Arr[] = {16, 17, 4, 3, 5, 2}
Output:
17 5 5 5 2 -1

Example 2:

Input:
N = 4
Arr[] = {2, 3, 1, 9}
Output:
9 9 9 -1
'''

class Solution:

	def nextGreatest(self,arr, n):
		mx = arr[n-1]
		i=n-2
		while i>=0:
		    mx_nxt = max(mx, arr[i])
		    mx=max(mx,arr[i+1])
		    arr[i]= mx
		    mx=mx_nxt
		    i-=1
		arr[-1]=-1
		return arr
	
# -------- Time and Space Complexity
'''
Time Complexity: O(n)
Due to a single iteration through the array, the time complexity is O(n).
Space complexity: O(1)
Since no additional space is required, the space complexity remains constant.
'''