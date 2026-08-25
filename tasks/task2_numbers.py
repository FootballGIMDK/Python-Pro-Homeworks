def square(number: int) -> int:
    return number ** 2

def sum_numbers(num1: int | float, num2: int | float) -> int | float:
    return num1 + num2

def dividing_operations(num1: int, num2: int) -> tuple[int, int]:
    #Comment just for clarification, use here if just cos I want to divide larger number to the smaller
    if num1 >= num2:
        return num1 // num2, num1 % num2
    else:
        return num2 // num1, num2 % num1

if __name__ == "__main__":
    print(square(5))
    print(sum_numbers(10, 3))
    print(dividing_operations(10, 3))