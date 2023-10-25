'''
https://practice.geeksforgeeks.org/problems/index-of-first-1-in-a-sorted-array-of-0s-and-1s4048/1?utm_source=geeksforgeeks&utm_medium=ml_article_practice_tab&utm_campaign=article_practice_tab

Given a sorted array consisting 0’s and 1’s. The problem is to find the index of first ‘1’ in the sorted array. It could be possible that the array consists of only 0’s or only 1’s. If 1’s are not present in the array then print “-1”.

Examples : 

Input : arr[] = {0, 0, 0, 0, 0, 0, 1, 1, 1, 1}
Output : 6

Input : arr[] = {0, 0, 0, 0}
Output : -1
'''

class Solution:
    def firstIndex(self, arr, n):
        beg=0
        end=n-1
        mid=0
        while beg<=end:
            mid = (beg+end)//2
            if arr[mid]==1 and (mid==0 or arr[mid-1]==0):
                return mid
            elif arr[mid]==1:
                end=mid-1
            else:
                beg=mid+1
        return -1
    
'''
Time Complexity: O(Log(n))
The solution is based on binary search, so there are Log(n) nunber of steps.
Space complexity: O(1)
Since no additional space is required, the space complexity remains constant.
'''
