def merge_sort(lst: list) -> list:
    if len(lst) > 1:
        middle_number = len(lst) // 2
        first_part = lst[:middle_number]
        second_part = lst[middle_number:]

        merge_sort(first_part)
        merge_sort(second_part)

        x, y, z = 0, 0, 0

        while x < len(first_part) and y < len(second_part):
            if first_part[x] <= second_part[y]:
                lst[z] = first_part[x]
                x += 1
            else:
                lst[z] = second_part[y]
                y += 1
            z += 1

        while x < len(first_part):
            lst[z] = first_part[x]
            x += 1
            z += 1

        while y < len(second_part):
            lst[z] = second_part[y]
            y += 1
            z += 1

    return lst


def bubble_sort(lst):
    for i in range(len(lst)):
        for j in range(0, len(lst) - i - 1):
            if lst[j] > lst[j + 1]:
                lst[j], lst[j + 1] = lst[j + 1], lst[j]
    return lst
