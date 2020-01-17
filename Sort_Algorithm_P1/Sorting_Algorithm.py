# Define Bubble Sort
def bubble_sort(array):
    print("\n","Bubble Sort")
    n = len(array)
    count_step = 0
    for i in range(n):
        for j in range(0, n - i - 1):
            # traverse the array from 0 to n-i-1
            if array[j] > array[j + 1]:
            # Swap if the element found is greater
                array[j], array[j + 1] = array[j + 1], array[j]
        count_step += 1
        print(count_step, array)
    print("\n", "Sorted Array")
    print(array)

# Define Selection Sort
def selection_sort(array):
    print("\n","Selection Sort")
    count_step = 0
    for i in range(len(array)):
        # Find the minimum element in remaining
        # unsorted array
        min_index = i
        for j in range(i + 1, len(array)):
            if array[min_index] > array[j]:
                min_index = j
                # Swap the found minimum element with
                # the first element
        array[i], array[min_index] = array[min_index], array[i]
        count_step += 1
        print(count_step, array)
    print("\n", "Sorted Array")
    print(array)

# Define Insertion Sort
def insertion_sort(array):
    print("\n","Insertion Sort")
    count_step = 0
    # Traverse through 1 to len(arr)
    for i in range(1, len(array)):
        key = array[i]
        # Move elements of array[0..i-1], that are
        # greater than key, to one position ahead
        # of their current position
        j = i - 1
        while j >= 0 and key < array[j]:
            array[j + 1] = array[j]
            j -= 1
        array[j + 1] = key
        count_step += 1
        print(count_step, array)
    print("\n", "Sorted Array")
    print(array)