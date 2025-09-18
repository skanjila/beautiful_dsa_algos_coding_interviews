from typing import List

def median_two_sorted_merge(first_array: List[int], second_array: List[int]) -> float:
    """
    Finds the median of two sorted arrays by merging them.
    Args:
        first_array: The first sorted list of integers.
        second_array: The second sorted list of integers.
    Returns:
        The median of the two sorted arrays as a float.
    """

    if not first_array and not second_array:
        raise ValueError("Both input arrays are empty; median is undefined.")
    length_first_array = len(first_array)
    length_second_array = len(second_array)

    fist_array_counter = 0
    second_array_counter = 0

    merged_array = []

    # while the counters of the first and second arrays have not reached the lengths
    # of both arrays either merge the current element into the first or the second array
    while fist_array_counter < length_first_array and second_array_counter < length_second_array:
        if first_array[fist_array_counter] <= second_array[second_array_counter]:
            merged_array.append(first_array[fist_array_counter])
            fist_array_counter += 1
        else:
            merged_array.append(second_array[second_array_counter])
            second_array_counter += 1
    # merge in the rest of the elements for both arrays
    merged_array.extend(first_array[fist_array_counter:])
    merged_array.extend(second_array[second_array_counter:])

    # retrieve the length of the newly merged array
    length_of_merged_array = len(merged_array)

    # now calculate the median based on whether the length
    # of the merged array is odd or even
    mid = length_of_merged_array // 2
    if length_of_merged_array % 2 == 1:
        return float(merged_array[mid])
    else:
        return (merged_array[mid - 1] + merged_array[mid]) / 2.0