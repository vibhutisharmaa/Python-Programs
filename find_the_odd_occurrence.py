'''
https://practice.geeksforgeeks.org/problems/find-the-odd-occurence4820/1?utm_source=geeksforgeeks&utm_medium=ml_article_practice_tab&utm_campaign=article_practice_tab

Given an array of positive integers. All numbers occur an even number of times except one number which occurs an odd number of times. Find the number 

Examples : 

Input : arr = {1, 2, 3, 2, 3, 1, 3}
Output : 3

Input : arr = {5, 7, 2, 7, 5, 2, 5}
Output : 5
'''

# -------- Approach 1
class Solution:
    def getOddOccurrence(self, arr, n):
        res = {}
        for i in arr:
            if i in res.keys():
                if res[i]==1:
                    res[i]=0
                else:
                    res[i]=1
            else:
                res[i]=1
        for key, val in res.items():
            if val!=0:
                return key
        return
    
# -------- Time and Space Complexity
'''
Time Complexity: O(n)
Due to a single iteration through the array and the dictionary, the time complexity is O(n).
Space complexity: O(n)
Since all the elements are stored in the dictionary.
'''

# -------- Approach 2 (Expected)
class Solution:
    def getOddOccurrence(self, arr, n):
        res=arr[0]
        for i in range(1, n):
            res^=arr[i]
        return res

# -------- Time and Space Complexity
'''
Time Complexity: O(n)
Due to a single iteration through the array, the time complexity is O(n).
Space complexity: O(1)
Since no additional space is required, the space complexity remains constant.
'''