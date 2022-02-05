## Problem 3: Rearrange Array Digits
Rearrange Array Elements so as to form two number such that their sum is maximum. Return these two numbers. You can assume that all array elements are in the range [0, 9]. The number of digits in both the numbers cannot differ by more than 1. You're not allowed to use any sorting function that Python provides and the expected time complexity is O(nlog(n)).

### Efficiency
The code sorts the provided list of numbers using the merge sort algorithm. Once the array is sorted, we can iterate over the numbers and append them alternately to the final output numbers. 

The time complexity of the sorting algorithm is O(nlogn) and the space complexity O(n). 