'''
https://practice.geeksforgeeks.org/problems/implement-queue-using-array/1

Implement a Queue using an Array. Queries in the Queue are of the following type:
(i) 1 x   (a query of this type means  pushing 'x' into the queue)
(ii) 2     (a query of this type means to pop element from queue and print the poped element)

Example 1:
Input:
Q = 5
Queries = 1 2 1 3 2 1 4 2
Output: 2 3

Example 2:
Input:
Q = 4
Queries = 1 3 2 2 1 4   
Output: 3 -1
'''

class MyQueue:
    
    def __init__(self):
        self.q = []
        self.front = 0
        self.rear = 0
        self.size = 100000
        
    #Function to push an element x in a queue.
    def push(self, x):
        if len(self.q)<=self.size:
            self.q.append(x)
            self.rear += 1 
   

    #Function to pop an element from queue and return that element.
    def pop(self): 
        if self.rear<=self.front:
            self.q=[]
            self.front=0
            self.rear=0
            return -1
        self.front+=1
        return self.q[self.front-1]