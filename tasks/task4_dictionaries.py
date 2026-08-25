def get_dictionary_keys(dictionary: dict):
    return dictionary.keys()

def get_united_dictionary(dictionary1: dict, dictionary2: dict) -> dict:
    resulting_dictionary = dictionary1 | dictionary2
    return resulting_dictionary

if __name__ == "__main__":
    print(get_dictionary_keys({'age': 20, 'name': 'tommy'}))
    print(get_united_dictionary({'age': 20, 'name': 'Tommy'}, {'height': 180, 'gender': 'male'}))
