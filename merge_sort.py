def merge_lists(left_sublist,right_sublist):
	i,j = 0,0
	result = []
	#iterate through both left and right sublist
	while i<len(left_sublist) and j<len(right_sublist):
		#if left value is lower than right then append it to the result
		if left_sublist[i] <= right_sublist[j]:
			result.append(left_sublist[i])
			i += 1
		else:
			#if right value is lower than left then append it to the result
			result.append(right_sublist[j])
			j += 1
	#concatenate the rest of the left and right sublists
	result += left_sublist[i:]
	result += right_sublist[j:]
	#return the result
	return result

def merge_sort(dataset):
	#if list contains only 1 element return it
	if len(dataset) <= 1:
		return dataset
	else:
		#split the lists into two sublists and recursively split sublists
		midpoint = int(len(dataset)/2)
		left_sublist = merge_sort(dataset[:midpoint])
		right_sublist = merge_sort(dataset[midpoint:])
		#return the merged list using the merge_list function above
		return merge_lists(left_sublist,right_sublist)
