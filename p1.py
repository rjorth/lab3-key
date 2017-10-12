def unique(list):
    singles_list = []
    for element in list:
        if element not in singles_list:
            singles_list.append(element)
    return singles_list
