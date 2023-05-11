def bubblesort(dataset):
    for iteration in range(len(dataset)-1, 0, -1):
        swapped = False
        for index in range(iteration):
            if dataset[index] > dataset[index+1]:
                dataset[index], dataset[index+1] = dataset[index+1], dataset[index]
                swapped = True
        if swapped == False:
            break;
    return dataset