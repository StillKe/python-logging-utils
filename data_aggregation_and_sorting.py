def bubble_sort(data):
    """
    Bubble sort algorithm to sort data in ascending order.

    Parameters:
        data: list
            The list of values to be sorted.

    Returns:
        list: The sorted list of values.
    """
    n = len(data)
    for i in range(n):
        for j in range(0, n-i-1):
            if data[j] > data[j+1]:
                data[j], data[j+1] = data[j+1], data[j]
    return data

def selection_sort(data):
    """
    Selection sort algorithm to sort data in ascending order.

    Parameters:
        data: list
            The list of values to be sorted.

    Returns:
        list: The sorted list of values.
    """
    n = len(data)
    for i in range(n-1):
        min_index = i
        for j in range(i+1, n):
            if data[j] < data[min_index]:
                min_index = j
        data[i], data[min_index] = data[min_index], data[i]
    return data

def insertion_sort(data):
    """
    Insertion sort algorithm to sort data in ascending order.

    Parameters:
        data: list
            The list of values to be sorted.

    Returns:
        list: The sorted list of values.
    """
    n = len(data)
    for i in range(1, n):
        key = data[i]
        j = i - 1
        while j >= 0 and data[j] > key:
            data[j + 1] = data[j]
            j -= 1
        data[j + 1] = key
    return data

def quick_sort(data):
    """
    Quick sort algorithm to sort data in ascending order.

    Parameters:
        data: list
            The list of values to be sorted.

    Returns:
        list: The sorted list of values.
    """
    if len(data) <= 1:
        return data
    pivot = data[len(data) // 2]
    left = [x for x in data if x < pivot]
    middle = [x for x in data if x == pivot]
    right = [x for x in data if x > pivot]
    return quick_sort(left) + middle + quick_sort(right)

def merge_sort(data):
    """
    Merge sort algorithm to sort data in ascending order.

    Parameters:
        data: list
            The list of values to be sorted.

    Returns:
        list: The sorted list of values.
    """
    if len(data) <= 1:
        return data
    middle = len(data) // 2
    left = merge_sort(data[:middle])
    right = merge_sort(data[middle:])
    return merge(left, right)

def merge(left, right):
    """
    Helper function for merge sort to merge two sorted lists.

    Parameters:
        left: list
            The left half of the list to be merged.
        right: list
            The right half of the list to be merged.

    Returns:
        list: The merged and sorted list.
    """
    result = []
    left_index, right_index = 0, 0
    while left_index < len(left) and right_index < len(right):
        if left[left_index] < right[right_index]:
            result.append(left[left_index])
            left_index += 1
        else:
            result.append(right[right_index])
            right_index += 1
    result.extend(left[left_index:])
    result.extend(right[right_index:])
    return result

def aggregate_data(*data_sources, sorting_technique='bubble'):
    """
    Aggregate data from multiple sources and sort using the specified technique.

    Parameters:
        *data_sources: tuple
            Variable number of data sources containing values to be aggregated.
        sorting_technique: str, optional
            The sorting technique to use ('bubble', 'selection', 'insertion', 'quick', 'merge').
            Default is 'bubble'.

    Returns:
        list: A list containing the aggregated and sorted values from all data sources.
    """
    # Aggregate data from all sources
    aggregated_data = []
    for source in data_sources:
        aggregated_data.extend(source)

    # Sort the aggregated data using the specified technique
    if sorting_technique == 'bubble':
        sorted_data = bubble_sort(aggregated_data)
    elif sorting_technique == 'selection':
        sorted_data = selection_sort(aggregated_data)
    elif sorting_technique == 'insertion':
        sorted_data = insertion_sort(aggregated_data)
    elif sorting_technique == 'quick':
        sorted_data = quick_sort(aggregated_data)
    elif sorting_technique == 'merge':
        sorted_data = merge_sort(aggregated_data)
    else:
        print("Invalid sorting technique. Using default (bubble sort).")
        sorted_data = bubble_sort(aggregated_data)

    return sorted_data

if __name__ == "__main__":
    data_sources = []
    while True:
        user_input = input("Enter data (separate values by spaces, leave empty to finish): ")
        if not user_input:
            break
        try:
            data = [int(x) for x in user_input.split()]
            data_sources.append(data)
        except ValueError:
            print("Invalid input. Please enter integers separated by spaces.")

    sorting_technique = input("Enter sorting technique ('bubble', 'selection', 'insertion', 'quick', 'merge'): ")
    sorted_data = aggregate_data(*data_sources, sorting_technique=sorting_technique)
    print("Sorted Data:", sorted_data)
