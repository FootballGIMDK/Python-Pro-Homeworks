def even_or_odd(number: int) -> str:
    if number % 2 == 0:
        return 'even'
    else:
        return 'odd'

def left_only_even_from_list(user_list: list) -> list:
    even_list = []
    for item in user_list:
        if item % 2 == 0:
            even_list.append(item)
    return even_list

if __name__ == "__main__":
    print(even_or_odd(1))
    print(even_or_odd(2))
    print(left_only_even_from_list([1, 2, 3, 4, 5, 6, 7]))