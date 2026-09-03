def square(number: int) -> int:
    """Function to square a number"""
    return number**2


def sum_numbers(num1: float, num2: float) -> float:
    """Function to sum two numbers"""
    return num1 + num2


def dividing_operations(num1: int, num2: int) -> tuple[int, int]:
    """Function to divide two numbers, always will divide larger number to smaller number"""
    return (num1 // num2, num1 % num2) if num1 >= num2 else (num2 // num1, num2 % num1)


if __name__ == "__main__":
    print(square(5))
    print(sum_numbers(10, 3))
    print(dividing_operations(10, 3))
