## Problem 1: Square Root of an Integer
Find the square root of the integer without using any Python library. You have to find the floor value of the square root.  

### Efficiency
The time complexity of the sqrt()-function is O(log(n)) because we make use of the binary search algorithm. The best-case would be O(1) when the first guess directly matches the desired output. The binary search approach repeats cutting the search space in half. After evaluating the current mid-value of the search space, we discard the irrelevant half. At some point, we have narrowed the search space down until we finally get the desired value.

As this iterative approach needs constant space, the space complexity is O(1).