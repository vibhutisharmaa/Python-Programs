'''
https://practice.geeksforgeeks.org/problems/first-and-last-occurrences-of-x2041/1?utm_source=geeksforgeeks&utm_medium=ml_article_practice_tab&utm_campaign=article_practice_tab

Given a sorted array arr[] with possibly duplicate elements, the task is to find indexes of the first and last occurrences of an element x in the given array. 

Example: 

Input : arr[] = {1, 3, 5, 5, 5, 5, 67, 123, 125}, x = 5
Output : First Occurrence = 2 Last Occurrence = 5
'''

class Solution: 
    
    def first_ind(self, arr,n,x):
        beg=0
        end = n-1
        while beg<=end:
            mid=(beg+end)//2
            if arr[mid]==x and (mid==0 or arr[mid-1]!=x):
                return mid
            elif arr[mid]>=x:
                end=mid-1
            else:
                beg=mid+1
        return -1
        
    def last_ind(self, arr,n,x):
        beg=0
        end = n-1
        while beg<=end:
            mid=(beg+end)//2
            if arr[mid]==x and (mid==n-1 or arr[mid+1]!=x):
                return mid
            elif arr[mid]<=x:
                beg=mid+1
            else:
                end=mid-1
        return -1
    
    def firstAndLast(self, arr, n, x): 
        if self.first_ind(arr,n,x) ==-1 and self.last_ind(arr,n,x) == -1:
            return [self.last_ind(arr,n,x)]
        return self.first_ind(arr,n,x), self.last_ind(arr,n,x)

'''
Time Complexity: O(Log(n))
The solution is based on binary search, so there are Log(n) nunber of steps.
Space complexity: O(1)
Since no additional space is required, the space complexity remains constant.
'''
