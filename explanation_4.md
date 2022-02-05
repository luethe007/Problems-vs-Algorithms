## Problem 4: Dutch National Flag Problem
Given an input array consisting on only 0, 1, and 2, sort the array in a single traversal. You're not allowed to use any sorting function that Python provides.

### Efficiency
The code runs through the array in a single traversal O(n). It uses pointers to keep track of the 0 and 2 positions and re-arranges them directly in the array.