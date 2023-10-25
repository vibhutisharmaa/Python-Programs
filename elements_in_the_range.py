'''

https://practice.geeksforgeeks.org/problems/elements-in-the-range2834/1?utm_source=geeksforgeeks&utm_medium=article_practice_tab&utm_campaign=article_practice_tab

Given an array arr[] containing positive elements. A and B are two numbers defining a range. The task is to check if the array contains all elements in the given range.

Example 1:

Input: N = 7, A = 2, B = 5
arr[] =  {1, 4, 5, 2, 7, 8, 3}
Output: Yes

Example 2:

Input: N = 7, A = 2, B = 6
arr[] = {1, 4, 5, 2, 7, 8, 3}
Output: No
'''

# -------- Approach 1
class Solution:
    def check_elements(self, arr, n, a, b):
        chk = {}
        for i in range(a,b+1):
            chk[i]=1
        for i in arr:
            if i>=1 and i<=b:
                chk[i]=0
        for key, value in chk.items():
            if value!=0:
                return 0
        return 1

# -------- Time and Space Complexity
'''
Time Complexity: O(n)
Due to a single iteration through the array and the dictionary, the time complexity is O(n).
Space complexity: O(b-a)
Since a dictionary of size equals to range a to b is utilised, the space complecity is O(b-a)
'''

# -------- Approach 2 (Expected)
class Solution:
    def check_elements(self, arr, n, a, b):
        for i in range(len(arr)):
            if abs(arr[i]) >= a and abs(arr[i]) <= b: 
                z = abs(arr[i]) - a
                if (arr[z] > 0) : 
                    arr[z] = arr[z] * -1
        for i in range(b-a+1):
            if arr[i]>0:
                return 0
        return 1
    
# -------- Time and Space Complexity
'''
Time Complexity: O(n)
Due to a single iteration through the array, the time complexity is O(n).
Space complexity: O(1)
Since no additional space is required, the space complexity remains constant.
'''
                
        