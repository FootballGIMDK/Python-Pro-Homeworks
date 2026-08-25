def get_list_average(user_list: list) -> float:
    return sum(user_list) / len(user_list)

def get_identical_elems(user_list1: list, user_list2: list) -> list:
    return list(set(user_list1) & set(user_list2))

if __name__ == "__main__":
    print(get_list_average([1, 2, 3, 4, 5]))
    print(get_identical_elems([1, 2, 3, 4, 5], [3, 4, 5, 6, 7]))
