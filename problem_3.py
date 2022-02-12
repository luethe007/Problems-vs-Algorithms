# %%
def rearrange_digits(input_list: list):
    """
    Rearrange Array Elements so as to form two number such that their sum is maximum.

    Args:
       input_list(list): Input List
    Returns:
       (int),(int): Two maximum sums
    """
    if not isinstance(input_list, list):
        raise ValueError("Please insert a list.")    

    # Check for valid input
    if len(input_list) <= 1:
        raise ValueError("Please insert a list with at least two numbers.")

    # Initialize emtpy strings for the numbers
    int_a = ''
    int_b = ''
    x = mergeSort(input_list)
    i = 0
    # Append the numbers to the int_a and int_b strings
    for number in x[::-1]:
        if number < 0 or number > 9:
            raise ValueError("Please insert a list with numbers in the range [0-9].")
        if i % 2 == 0:
            int_a += str(number)
        else:
            int_b += str(number)
        i += 1
    return [int(int_a), int(int_b)]


# Python program for implementation of MergeSort
def mergeSort(arr):
    """
        Sorts array in ascending order.
        Code Source (slightly adapted): https://www.geeksforgeeks.org/merge-sort/
    """
    if len(arr) > 1:
  
         # Finding the mid of the array
        mid = len(arr)//2
  
        # Dividing the array elements
        L = arr[:mid]
  
        # into 2 halves
        R = arr[mid:]
  
        # Sorting the first half
        mergeSort(L)
  
        # Sorting the second half
        mergeSort(R)
  
        i = j = k = 0
  
        # Copy data to temp arrays L[] and R[]
        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1
  
        # Checking if any element was left
        while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1
  
        while j < len(R):
            arr[k] = R[j]
            j += 1
            k += 1
    return arr

def test_function(test_case):
    output = rearrange_digits(test_case[0])
    solution = test_case[1]
    if sum(output) == sum(solution):
        print("Pass")
    else:
        print("Fail")

# %% 
test_function([[1, 2, 3, 4, 5], [542, 31]])
test_function([[4, 6, 2, 5, 9, 8], [964, 852]])
test_function([[], "ValueError"]) # Edge case: Value Error due to invalid input
test_function([[1,-2,-2,5], "ValueError"]) # Value Error due to invalid numbers
test_function([None, 10]) # Edge case: None input
# %%
