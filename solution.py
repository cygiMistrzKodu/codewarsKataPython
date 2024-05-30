import heapq


def sum_two_smallest_numbers(numbers: [int]):
    smallest_two_numbers = heapq.nsmallest(2, numbers)
    return sum(smallest_two_numbers)
