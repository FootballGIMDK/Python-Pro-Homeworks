def united_sets(set1: set[int], set2: set[int]) -> set[int]:
    """Function to return united set of two sets"""
    return set1 | set2


def check_if_set_contains(set1: set[int], set2: set[int]) -> bool:
    """Function to check if second set are contained in first set"""
    return set2.issubset(set1)


if __name__ == "__main__":
    print(united_sets({1, 2, 3}, {3, 4, 5}))
    print(check_if_set_contains({1, 2, 3, 4, 5, 6, 7}, {3, 4, 5}))
    print(check_if_set_contains({1, 2, 3, 4, 5, 6, 7}, {3, 4, 5, 8}))
