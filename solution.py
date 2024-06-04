class OddNumberSorter:
    def __init__(self, odd_number_list):
        self.odd_number_list = odd_number_list
        self.odd_number_list.sort()

    next_odd_number_index = 0

    def next_number(self):
        odd_number = self.odd_number_list[self.next_odd_number_index]
        self.next_odd_number_index += 1
        return odd_number


def sort_array(source_array: list[int]):
    only_odd_numbers = [number for number in source_array if number % 2 != 0]

    odd_number_sorter = OddNumberSorter(only_odd_numbers)

    sorted_odd_numbers = [number if (number % 2 == 0) else odd_number_sorter.next_number() for number in source_array]

    return sorted_odd_numbers
