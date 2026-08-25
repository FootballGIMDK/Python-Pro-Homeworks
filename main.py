from tasks.task1_strings import count_string_length, strings_concatenation
from tasks.task2_numbers import square, sum_numbers, dividing_operations
from tasks.task3_lists import get_list_average, get_identical_elems
from tasks.task4_dictionaries import get_dictionary_keys, get_united_dictionary
from tasks.task5_sets import united_sets, check_if_set_contains
from tasks.task6_for_if import even_or_odd, left_only_even_from_list

def main():
    print("Homework 3:")
    print("Task 1:")
    str1 = input("Enter the first string: ")
    str2 = input("Enter the second string: ")
    str1_length = count_string_length(str1)
    result_string = strings_concatenation(str1, str2)
    print(f"Task 1 - first string length: {str1_length}")
    print(f"Task 1 - concatenated strings: {result_string}")
    print("Task 2:")
    num1 = int(input("Enter the first integer number: "))
    num2 = int(input("Enter the second integer number: "))
    integer_division_part, reminder = dividing_operations(num1, num2)
    print(f"Task 2 - first number square: {square(num1)}")
    print(f"Task 2 - sum of the numbers: {sum_numbers(num1, num2)}")
    print(f"Task 2 - integer_division_part: {integer_division_part}, reminder: {reminder}")
    print("Task 3:")
    list1 = [num1, num2]
    list2 = [num1, num2]
    for _ in range(3):
        number = int(input("Enter the int number for lists: "))
        list1.append(number)
        list2.insert(0, number)
    print(f"Task 3 - average value for list1: {get_list_average(list1)}")
    print(f"Task 3 - list of identical elements: {get_identical_elems(list1, list2)}")
    dict1 = {}
    dict2 = {}
    print("Task 4: Enter Keys and Values for dict1")
    for _ in range(2):
        key = input("Key dict1: ")
        value = input("Value dict1: ")
        dict1[key] = value
    print("Task 4: Enter Keys and Values for dict2")
    for _ in range(2):
        key = input("Key dict: ")
        value = input("Value dict: ")
        dict2[key] = value
    print(f"Task 4 - keys of the dict1: {get_dictionary_keys(dict1)}")
    print(f"Task 4 - united dictionary: {get_united_dictionary(dict1, dict2)}")
    print("Task 5: Using existing lists as sets")
    set1 = set(list1)
    set2 = set(list2)
    print(f"Task 5 - united sets: {united_sets(set1, set2)}")
    print(f"Task 5 - set 2 is a subset of the set2: {check_if_set_contains(set1, set2)}")
    print("Task 6: Using existing numbers")
    print(f"Task 6 - Number {num1} is: {even_or_odd(num1)}")
    print(f"Task 6 - Even numbers from {list1} is: {left_only_even_from_list(list1)}")
    lambda_even_or_odd = lambda n: "even" if n % 2 == 0 else "odd"
    print(f"Task 7 - Lambda func which check even or odd for {num2} say: this is {lambda_even_or_odd(num2)}")

if __name__ == "__main__":
    main()