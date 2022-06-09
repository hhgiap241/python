def heapify(arr, n, i):
    parent = int(((i-1)/2))
    # For Max-Heap
    # If current node is greater than its parent
    # Swap both of them and call heapify again
    # for the parent
    if arr[parent] > 0:
        if arr[i] > arr[parent]:
            arr[i], arr[parent] = arr[parent], arr[i]
            # Recursively heapify the parent node
            heapify(arr, n, parent)
  
  
def them_vao_heap(arr, key):
    n = len(arr)
    # Increase the size of Heap by 1
    n += 1
    # Insert the element at end of Heap
    arr.append(key)
    # Heapify the new node following a
    # Bottom-up approach
    heapify(arr, n, n-1)
  
# Driver code to test above
arr = [ 190, 178, 145, 154, 54, 110, 137]
them_vao_heap(arr, 160)
n = len(arr)
print ("Sorted array is")
for i in range(n):
    print ("%d" %arr[i]),