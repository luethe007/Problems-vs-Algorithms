## Problem 6: Unsorted Integer Array
In this problem, we will look for smallest and largest integer from a list of unsorted integers. The code should run in O(n) time. Do not use Python's inbuilt functions to find min and max.


### Efficiency
We iterate over the input list once O(n). First, we set the min and max value variables to the first element of the list and compare each further element with these variables. If the current number is lower /higher than the corresponding variables, the number sets this variable.