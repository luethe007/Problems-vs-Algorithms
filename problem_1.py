# %%
def sqrt(n):
   """
   Calculate the floored square root of a number.

   Args:
      number(int): Number to find the floored squared root
   Returns:
      int: Floored Square Root
   """
   # Check for negative values
   if n < 0:
      raise ValueError("There is no square root of a negative number.")

   # Check base cases
   if n < 2:
      return n

   # Initialize search space
   output = 0
   lower = 1
   higher = n // 2

   # Iterate over search space using binary search
   while lower <= higher:
      mid = (lower + higher) // 2
      sqr = mid*mid
      
      # Return mid if perfect match
      if sqr == n:
         return mid
      # Continue with right side of the search space
      elif sqr < n:
         lower = mid + 1
         output = mid
      # Continue with left side of the search space
      else:
         higher = mid - 1

   # return output
   return output

# %%
print("Pass" if  (3 == sqrt(9)) else "Fail")
print("Pass" if  (0 == sqrt(0)) else "Fail")
print("Pass" if  (4 == sqrt(16)) else "Fail")
print("Pass" if  (1 == sqrt(1)) else "Fail")
print("Pass" if  (5 == sqrt(27)) else "Fail")
try:
   sqrt(-27)
except ValueError:
   print("Pass")
print("Pass" if  (1014 == sqrt(1030000)) else "Fail")


# %%
