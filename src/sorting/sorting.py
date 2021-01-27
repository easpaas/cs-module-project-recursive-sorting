# # TO-DO: complete the helper function below to merge 2 sorted arrays
def merge(arrA, arrB):
    elements = len(arrA) + len(arrB)
    # initialize array with all zeros 
    merged_arr = [0] * elements

    # Your code here

    return merged_arr

# Recursive Merge Sort function
def merge_sort(arr):
    if len(arr) > 1:
      mid = len(arr)//2
      # arr split into halves
      L = arr[:mid]
      R = arr[mid:]
      # recursive call to split arr in halves
      merge_sort(L)
      merge_sort(R)

      # initalize i,j,k to 0
      i = j = k = 0

      # Copy data to temp arrays L[] and R[] 
      while i < len(L) and j < len(R): 
          if L[i] < R[j]: 
              arr[k] = L[i] 
              i+= 1
          else: 
              arr[k] = R[j] 
              j+= 1
          k+= 1
          
      # Checking if any element was left 
      while i < len(L): 
          arr[k] = L[i] 
          i+= 1
          k+= 1
          
      while j < len(R): 
          arr[k] = R[j] 
          j+= 1
          k+= 1

    return arr

# STRETCH: implement the recursive logic for merge sort in a way that doesn't 
# utilize any extra memory
# In other words, your implementation should not allocate any additional lists 
# or data structures; it can only re-use the memory it was given as input
def merge_in_place(arr, start, mid, end):
    # Your code here
  pass

def merge_sort_in_place(arr, l, r):
    # Your code here
  pass
