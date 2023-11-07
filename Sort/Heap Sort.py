def heapsort(lst):
  sort = []
  max_heap = MaxHeap()
  # Add items of an unsorted list into a max-heap.
  for idx in lst:
    max_heap.add(idx)
  # While there is at least one element in the heap, remove the root of the heap and place it at the beginning of a list that will hold the sorted values. Whenever the root is extracted, the heap must be rebalanced.
  while max_heap.count > 0:
    max_value = max_heap.retrieve_max()
    sort.insert(0, max_value)
  # Return the sorted list
  return sort

my_list = [99, 22, 61, 10, 21, 13, 23]
sorted_list = heapsort(my_list)
print(sorted_list) # Prints: [10, 13, 21, 22, 23, 61, 99]