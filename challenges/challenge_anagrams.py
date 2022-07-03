def partition(numbers, start, end):
    pivot = numbers[end]
    delimiter = start - 1

    for index in range(start, end):
        if numbers[index] <= pivot:
            delimiter += 1
            x, y = index, delimiter
            numbers[x], numbers[y] = numbers[y], numbers[x]

    numbers[delimiter + 1], numbers[end] = numbers[end], numbers[delimiter + 1]

    return delimiter + 1


def quick_sort(numbers, start, end):
    if start < end:
        p = partition(numbers, start, end)
        quick_sort(numbers, start, p - 1)
        quick_sort(numbers, p + 1, end)


def sort_string(string):
    letter_list = []
    for letter in string:
        letter_list.append(letter)
    quick_sort(letter_list, 0, len(letter_list) - 1)
    word = "".join(letter_list)

    return word


def is_anagram(first_string, second_string):
    first_word = sort_string(first_string.lower())
    second_word = sort_string(second_string.lower())
    return first_word == second_word
