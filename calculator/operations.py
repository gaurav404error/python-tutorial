# User defined library or module
from termcolor import colored # external module 

def add(x:int,y:int) -> None:
    result = x + y
    print(colored(f"Sum of {x} + {y} = {result}", "magenta"))
    
def subtract(x:int,y:int) -> None:
    result = x - y
    print(f"Difference between {x} - {y} = {result}")

def multiply(x:int,y:int) -> None:
    result = x * y
    print(f"Multiplication of {x} X {y} = {result}")

def decimal_division(x:int,y:int) -> None:
    result = x / y
    print(f"Divison of {x} / {y} = {result}")

def quotient(x:int,y:int) -> None:
    result = x // y
    print(f"Quotient of {x} // {y} = {result}")

def remainder(x:int,y:int) -> None:
    result = x % y
    print(f"Remainder of {x} % {y} = {result}")

def square_of(x:int) -> None:
    result = x ** 2
    print(f"Square of {x} = {result}")