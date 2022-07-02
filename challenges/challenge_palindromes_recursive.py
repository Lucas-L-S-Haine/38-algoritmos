def is_palindrome_recursive(word, low_index, high_index):
    if not word or word == "":
        return False
    elif word[low_index] != word[high_index]:
        return False
    elif high_index == low_index + 1:
        return word[low_index] == word[high_index]
    elif high_index == low_index:
        return True
    return is_palindrome_recursive(word, low_index + 1, high_index - 1)
