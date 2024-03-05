#!/usr/bin/python3
""" Function that finds 'a peak' in a list of unsorted integers"""


def quick_sort(array, low, high):
    if (low < high):
        parti = lomutoPartition(array, low, high)
        quick_sort(array, low, parti - 1)
        quick_sort(array, parti + 1, high)


def lomutoPartition(unsorted_list, low, high):
    i = low - 1
    pivot = unsorted_list[high]
    for j in range(low, high):
        if unsorted_list[j] < pivot:
            i += 1
            unsorted_list[i], unsorted_list[j] = \
                unsorted_list[j], unsorted_list[i]
    unsorted_list[i + 1], unsorted_list[high] = \
        unsorted_list[high], unsorted_list[i + 1]

    return (i + 1)


def find_peak(array):
    if not array or array == []:
        return None
    elif len(array) == 1:
        return array[0]
    elif len(array) == 2:
        return max(array)
    quick_sort(array, 0, len(array) - 1)
    return array[-1]

