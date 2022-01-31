## Problem 2: Search in a Rotated Sorted Array
You are given a sorted array which is rotated at some random pivot point.

Example: [0,1,2,4,5,6,7] might become [4,5,6,7,0,1,2]

You are given a target value to search. If found in the array return its index, otherwise return -1.

### Efficiency
The provided solution recursively discards half of the array and thus uses binary search to find the index of the target. Therefore, the worst-case time complexity is O(log(n)).