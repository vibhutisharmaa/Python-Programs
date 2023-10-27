'''
https://practice.geeksforgeeks.org/problems/implement-strstr/1

Your task is to implement the function strstr. The function takes two strings as arguments (s,x) and  locates the occurrence of the string x in the string s. The function returns an integer denoting the first occurrence of the string x in s (0 based indexing).
Note: You are not allowed to use inbuilt function.

Example 1:

Input:
s = GeeksForGeeks, x = Fr
Output: -1

Example 2:

Input:
s = GeeksForGeeks, x = For
Output: 5
'''

def strstr(s,x):
    #code here
    i=0
    j=0
    k=0
    
    # ------ Optimised by traversing till (len(s)-len(x)) instead of len(s)
    while k<=(len(s)-len(x)):   
        i=k
        while k<len(s) and j<len(x) and s[k]==x[j]:
            j+=1
            k+=1
        if j==len(x):
            return i
        k=i+1
        j=0
    return -1

# -------- Time and Space Complexity
'''
Time Complexity: O(|s|*|x|)
Space complexity: O(1)
Since no additional space is required, the space complexity remains constant.
'''
            