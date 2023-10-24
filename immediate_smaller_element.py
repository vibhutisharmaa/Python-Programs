'''
Link: https://practice.geeksforgeeks.org/problems/immediate-smaller-element1142/1

Given an integer array. For each element in the array, check whether the right adjacent element of 
the array is smaller. If next element is smaller, update the current index to that element. If not, 
then  -1.

Example 1:
Input:
N = 5
Arr[] = {4, 2, 1, 5, 3}
Output:
2 1 -1 3 -1

Example 2:
Input:
N = 6
Arr[] = {5, 6, 2, 3, 1, 7}
Output:
-1 2 -1 1 -1 -1
'''

class Solution:
	def immediateSmaller(self,arr,n):
		# code here
		for i in range(0, len(arr)-1):
		    arr[i] = arr[i+1] if arr[i+1]<arr[i] else -1
		arr[-1]=-1
		return arr
