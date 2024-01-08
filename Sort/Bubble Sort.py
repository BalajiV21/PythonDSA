def bubbleSort(array):
  # access each element
  for a in range(len(array)):
     # compare array elements
    for b in range(0, len(array) - a - 1):
      # compare 
      if array[b] > array[b + 1]:
          
        # swapping elements
        temp = array[b]
        array[b] = array[b+1]
        array[b+1] = temp

#driver code
array = [5, 4, 2, 1, 3]
print("The original array is: ", array)

bubbleSort(array)
print('The Sorted Array is: ', array)
