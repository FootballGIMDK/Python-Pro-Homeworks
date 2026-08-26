def get_dictionary_keys(dictionary: dict[str, object]) -> list[str]:
    """Function to return all keys of the dictionary"""
    return list(dictionary.keys())


def get_united_dictionary(dictionary1: dict, dictionary2: dict) -> dict:
    """Function to return united dictionary of two dictionaries"""
    return dictionary1 | dictionary2


if __name__ == "__main__":
    print(get_dictionary_keys({"age": 20, "name": "tommy"}))
    print(
        get_united_dictionary(
            {"age": 20, "name": "Tommy"}, {"height": 180, "gender": "male"}
        )
    )
