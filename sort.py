from ship import Ship


def selection_sort_by_capacity(capacity_array):
    for a in range(len(capacity_array)):
        for b in range(a + 1, len(capacity_array)):
            if capacity_array[a].capacity > capacity_array[b].capacity:
                capacity_array[a], capacity_array[b] = capacity_array[b], capacity_array[a]
                Ship.change_count()
                Ship.compare_count()
    return capacity_array


def merge_sort_by_num_of_cases(num_of_cases_array):
    if len(num_of_cases_array) <= 1:
        return num_of_cases_array
    middle_array = int(len(num_of_cases_array) / 2)
    left_array = merge_sort_by_num_of_cases(num_of_cases_array[:middle_array])
    right_array = merge_sort_by_num_of_cases(num_of_cases_array[middle_array:])
    return merge(left_array, right_array)


def merge(left_array, right_array):
    array = []
    x = 0
    y = 0
    while x < len(left_array) and y < len(right_array):
        if left_array[x].num_of_cases <= right_array[y].num_of_cases:
            array.append(left_array[x])
            x += 1
        else:
            array.append(right_array[y])
            y += 1
            Ship.change_count()
            Ship.compare_count()
    array += left_array[x:]
    array += right_array[y:]
    return array