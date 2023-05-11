def partition(dataset,low,high): 
    i = ( low-1 )         # index of smaller element 
    pivot = dataset[high]     # pivot 
  
    for j in range(low , high): 
  
        # If current element is smaller than or equal to pivot 
        if   dataset[j] <= pivot: 
            # increment index of smaller element 
            i = i+1 
            dataset[i],dataset[j] = dataset[j],dataset[i] 
  
    dataset[i+1],dataset[high] = dataset[high],dataset[i+1] 
    return ( i+1 ) 
  
# The main function that implements QuickSort 
# dataset[] --> datasetay to be sorted, 
# low  --> Starting index, 
# high  --> Ending index 
  
# Function to do Quick sort 
def quickSort(dataset,low,high): 
    if len(dataset) <= 1:
        return dataset

    if low < high: 
        # pi is partitioning index, dataset[p] is now 
        # at right place 
        pi = partition(dataset,low,high) 
        # Separately sort elements before 
        # partition and after partition 
        quickSort(dataset, low, pi-1) 
        quickSort(dataset, pi+1, high) 
    return dataset