def even_or_odd(number: int) -> str:
    """Function to get an even or odd number"""
    return "even" if number % 2 == 0 else "odd"


def left_only_even_from_list(user_list: list[int]) -> list[int]:
    """Function to get a list of even numbers from a list"""
    return [item for item in user_list if item % 2 == 0]


if __name__ == "__main__":
    print(even_or_odd(1))
    print(even_or_odd(2))
    print(left_only_even_from_list([1, 2, 3, 4, 5, 6, 7]))
