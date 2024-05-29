def remove_every_other(my_list: list):
    return [element for index, element in enumerate(my_list) if index % 2 == 0]
