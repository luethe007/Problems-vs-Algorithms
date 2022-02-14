## Problem 4: Dutch National Flag Problem
Given an input array consisting on only 0, 1, and 2, sort the array in a single traversal. You're not allowed to use any sorting function that Python provides.

### Efficiency
We use Quicksort to solve this problem. The code runs through the array in a single traversal. It uses pointers to keep track of the 0 and 2 positions and re-arranges them directly in the array.
The time complexity is O(n) and the space complexity is O(1).