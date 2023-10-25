'''
https://practice.geeksforgeeks.org/problems/replace-all-0s-with-5/1?utm_source=geeksforgeeks&utm_medium=article_practice_tab&utm_campaign=article_practice_tab
Given an integer as input and replace all the ‘0’ with ‘5’ in the integer. 

Examples: 

Input: 102 
Output: 152

Input: 1020 
Output: 1525
'''

def convertFive(n):
    res=0
    dgt=1
    if n==0:
        return 5
    while n>0:
        r = n%10
        r = 5 if r==0 else r
        res+=r*dgt
        dgt*=10
        n=n//10
    return res

# -------- Time and Space Complexity
'''
Time Complexity: O(k)
where k: Number of digits in input integer (n).
Space complexity: O(1)
Since no additional space is required, the space complexity remains constant.
'''