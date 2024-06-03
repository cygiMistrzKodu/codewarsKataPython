def sum_array(arr: list[int]):
    if not arr:
        return 0

    if len(arr) == 1:
        return 0

    arr.remove(min(arr))
    arr.remove(max(arr))

    return sum(arr)
