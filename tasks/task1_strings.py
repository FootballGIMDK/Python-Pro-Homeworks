def count_string_length(string: str) -> int:
    """Function to count the number of characters in a string"""
    return len(string)


def strings_concatenation(str1: str, str2: str) -> str:
    """Function to concatenate two strings"""
    return str1 + str2


if __name__ == "__main__":
    print(count_string_length("Independence"))
    print(strings_concatenation("Independence ", "Day"))
