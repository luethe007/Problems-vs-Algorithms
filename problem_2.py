# %%
def rotated_array_search(input_list, target):
    """
        Find the index by searching in a rotated sorted array.

        Args:
            input_list(array), number(int): Input array to search and the target
        Returns:
            int: Index or -1
    """
    # Call recursive search
    target_index = recursive_search(input_list, 0, len(input_list)-1, target)
    return target_index

def recursive_search(input_list, low, high, target):
    # Invalid base case
    if low > high:
        return -1
    
    # Check mid element
    mid = (low + high) // 2
    if input_list[mid] == target:
        return mid
 
    # Check if input_list[low:mid] is sorted
    if input_list[low] <= input_list[mid]:
        # Check if target in left half
        if target >= input_list[low] and target <= input_list[mid]:
            return recursive_search(input_list, low, mid-1, target)
        # Target not in left half, continue with right half
        return recursive_search(input_list, mid + 1, high, target)
 
    # input_list[low:mid] not sorted, but input_list[mid:high] is sorted
    # Check if target in right half
    if target >= input_list[mid] and target <= input_list[high]:
        return recursive_search(input_list, mid + 1, high, target)
    # Target not in right half, continue with left half
    return recursive_search(input_list, low, mid-1, target)

def linear_search(input_list, number):
    for index, element in enumerate(input_list):
        if element == number:
            return index
    return -1

def test_function(test_case):
    input_list = test_case[0]
    number = test_case[1]
    if linear_search(input_list, number) == rotated_array_search(input_list, number):
        print("Pass")
    else:
        print("Fail")


# %%
test_function([[6, 7, 8, 9, 10, 1, 2, 3, 4], 6])
test_function([[6, 7, 8, 9, 10, 1, 2, 3, 4], 1])
test_function([[6, 7, 8, 1, 2, 3, 4], 8])
test_function([[6, 7, 8, 1, 2, 3, 4], 1])
test_function([[6, 7, 8, 1, 2, 3, 4], 10])

# %%
