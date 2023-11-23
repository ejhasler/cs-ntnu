# Weighted Job Scheduling - Algorithm and Data Structures 2 at DTU Copenhagen
# Naive Recursive Method

# Importing the following module to sort array
# based on our custom comparison function
from functools import cmp_to_key

# A job has start time, finish time and profit.
class Job:

    def __init__(self, start, finish, profit):
        
        self.start = start
        self.finish = finish
        self.profit = profit

# A utiltiy function that is used for
# sorting events accoring to finish time
def jobComparator(s1, s2):

    return s1.finish < s2.finish

# Find the latest job (in sorted array) that
# doesn't conflict with the job[i]. If there
# is no compatible job, then it returns -1.
def latestNonConflict(arr, i):

    for j in range(i - 1, -1, -1):
        if arr[j].finish <= arr[i - 1].start:
            return j
        
    return -1

# A recursive function that returns the
# maximum possible profit from given
# array of jobs. The array of jobs must
# be sorted according to finish time
def findMaxProfitRec(arr, n):

    # Base case
    if n == 1:
        return arr[n - 1].profit
    
    # Find profit when current job is included
    inclProf = arr[n - 1].profit
    i = latestNonConflict(arr, n)

    if i != -1:
        inclProf += findMaxProfitRec(arr, i + 1)

    # Find profit when current job is excluded
    exclProf = findMaxProfitRec(arr, n - 1)
    return max(inclProf, exclProf)

# The main function that returns the maximum
# possible profit from given array of jobs
def findMaxProfit(arr, n):
     
    # Sort jobs according to finish time
    arr = sorted(arr, key = cmp_to_key(jobComparator))
    return findMaxProfitRec(arr, n)
 
# Driver code
values = [ (1, 7, 4), (10, 12, 2), 
           (2, 5, 3), (8, 11, 4), (12, 13, 3), (3, 9, 5)
            , (3, 4, 3), (4, 6, 3), (5, 8, 2), (4, 13, 6) ]
arr = []
for i in values:
    arr.append(Job(i[0], i[1], i[2]))
     
n = len(arr)
 
print("The optimal profit is", findMaxProfit(arr, n))