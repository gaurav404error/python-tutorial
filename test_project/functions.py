def sum_numbers(numbers):
    total=0
    for x in numbers:
        total += x
        return total

def add_number(x:int, y:int) -> int:
    sum_of_numbers = x + y
    return sum_of_numbers

def greet(first_name:str) -> None:
    print(f"{first_name} loves India!")