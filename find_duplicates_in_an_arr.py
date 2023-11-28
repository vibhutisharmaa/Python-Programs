'''
https://practice.geeksforgeeks.org/problems/find-duplicates-in-an-array/1

Given an array a of size N which contains elements from 0 to N-1, you need to find all the elements occurring more than once in the given array. 
Return the answer in ascending order. If no such element is found, return list containing [-1]. 

Example 1:

Input:
N = 4
a[] = {0,3,1,2}
Output: -1

Example 2:

Input:
N = 5
a[] = {2,3,1,2,3}
Output: 2 3 
'''

def duplicates(self, arr, n): 
    chk = [0]*n
    res=[]
    for i in arr:
        chk[i]+=1
    for i in range(len(chk)):
        if chk[i]>1:
            res.append(i)
    if len(res)==0:
        return [-1]
    return res
    

# -------- Time and Space Complexity
'''
Time Complexity: O(n)
Two iterations through the given array
Space complexity: O(n)
Number of elements in the result array (worst case) = n/2 and 
size of the dictionary utilized = n
'''
            