def bubbleSort(arr):                       #initiate a function bubblesort
  n=len(arr)                                   
  for i in range(n):                              #traverse through all array elements  
                                                             #last  i elements found is greater
   for j in range(0,n-i-1):                   #traverse the array from  0 to n-i-1
                                                             #swap if element is greater                 
                                                             #than the next element
              if arr[j]>arr[j+1] :
                   arr[j], arr[j+1]=arr[j+1],arr[j]
#Driver code to test above
arr=[12,23,354,61,11,45,2]
bubbleSort(arr)
print("sorted array is:")
for i in range(len(arr)):
    print("%d" %arr[i])
