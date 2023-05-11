import random
import sys
import choose_sorting_algorithm
import bubble_sort
import merge_sort
import quick_sort
import time

startTime = time.time()
dataset = [random.randint(0, 100000) for _ in range(100000)]
sys.setrecursionlimit(100000)
bestSortingTechnique = choose_sorting_algorithm.choose_sorting_algorithm(dataset)

match bestSortingTechnique:
    case "bubble_sort":
        print("Using bubble sort for the dataset")
        print(bubble_sort.bubblesort(dataset))
    case "merge_sort":
        print("Using merge sort for the dataset")
        print(merge_sort.merge_sort(dataset))
    case "quick_sort":
        print("Using quick sort for the dataset")
        low = 0
        high = len(dataset)-1
        quick_sort.quickSort(dataset,low,high)
# print("Using bubble sort for the dataset")
# bubble_sort.bubblesort(dataset)
# endTime = time.time()
# print("Time taken for execution is",endTime-startTime)
# startTime = time.time()
# print("Using merge sort for the dataset")
# merge_sort.merge_sort(dataset)
# endTime = time.time()
# print("Time taken for execution is",endTime-startTime)
# startTime = time.time()
# print("Using quick sort for the dataset")
# low = 0
# high = len(dataset)-1
# quick_sort.quickSort(dataset,low,high)
endTime = time.time()
print("Time taken for execution is",endTime-startTime)