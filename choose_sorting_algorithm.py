def choose_sorting_algorithm(dataset):
  """Chooses the most efficient sorting algorithm for a given dataset.

  Args:
    dataset: The dataset to be sorted.

  Returns:
    The name of the sorting algorithm to use.
  """

  # Get the size of the dataset.
  size = len(dataset)

  # If the dataset is small, use a simple sorting algorithm.
  if size < 100:
    return "bubble_sort"

  # If the dataset is already sorted, use a stable sorting algorithm.
  if sorted(dataset) == dataset:
    return "merge_sort"

  # If the dataset is large, use a fast sorting algorithm.
  return "quick_sort"