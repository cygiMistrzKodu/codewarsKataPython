def remove_smallest(numbers: list[int]):
    if not numbers:
        return []

    smallest_rating = min(numbers)
    exhibits_without_lowest_rating = numbers.copy()
    try:
        exhibits_without_lowest_rating.remove(smallest_rating)
    except ValueError:
        return []

    return exhibits_without_lowest_rating
