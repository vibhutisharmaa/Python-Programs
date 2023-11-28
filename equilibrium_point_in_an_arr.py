'''
https://practice.geeksforgeeks.org/problems/find-duplicates-in-an-array/1

Given an array A of n positive numbers. The task is to find the first equilibrium point in an array. 
Equilibrium point in an array is an index (or position) such that the sum of all elements before that index is same as sum of elements after it.
Note: Return equilibrium point in 1-based indexing. Return -1 if no such point exists. 

Example 1:

n = 5 
A[] = {1,3,5,2,2} 
Output: 
3 

Example 2:

n = 1
A[] = {1} 
Output: 
1
'''

def equilibriumPoint(self,a, n):
    if n==1:
        return 1
    s1=a[0]
    s2=a[n-1]
    i=1
    j=n-2
    while i!=j and i<n and j>0:
        if s1>s2:
            s2+=a[j]
            j-=1
        else:
            s1+=a[i]
            i+=1
    if s1==s2:
        return i+1
    return -1
    

# -------- Time and Space Complexity
'''
Time Complexity: O(n)
Space complexity: O(1)
'''
            