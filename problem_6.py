# %%
def get_min_max(ints):
   """
   Return a tuple(min, max) out of list of unsorted integers.

   Args:
      ints(list): list of integers containing one or more integers
   """
   if not ints:
      raise ValueError("Please insert a valid list of integers.")
   min_val = ints[0]
   max_val = ints[0]

   for number in ints[1:]:
      if number < min_val:
         min_val = number
         continue
      if number > max_val:
         max_val = number
   return (min_val, max_val)

## Example Test Case of Ten Integers
import random

l = [i for i in range(0, 10)]  # a list containing 0 - 9
random.shuffle(l)

print ("Pass" if ((0, 9) == get_min_max(l)) else "Fail")

get_min_max([]) # Edge case: empty list
get_min_max(None) # Edge case: None input
get_min_max((1,3,21,2,2,0.4,333)) # Edge case: tuple as input
# %%
