'''
https://practice.geeksforgeeks.org/problems/find-duplicates-in-an-array/1

Given an expression string x. Examine whether the pairs and the orders of {,},(,),[,] are correct in exp.
For example, the function should return 'true' for exp = [()]{}{[()()]()} and 'false' for exp = [(]).

Example 1:

Input:
{([])}
Output: 
true

Example 2:

Input: 
([]
Output: 
false
'''

def ispar(self,x):
    mp = {'}': '{', ']':'[', ')': '('}
    chk = []
    for i in x:
        if i in ['{', '[', '(']:
            chk.append(i)
        elif i in ['}', ']', ')']:
            if len(chk)==0:
                return False
            temp = chk.pop()
            if temp != mp[i]:
                return False
    if len(chk)==0:
        return True
    return False
    

# -------- Time and Space Complexity
'''
Time Complexity: O(n)
Space complexity: O(n)
'''
            