from calculator_art import logo
def add(a, b):
    return a + b
def subtract(a, b):
    return a - b
def multiply(a, b):
    return a * b
def divide(a, b):
    if b == 0:
        return "Error: Division by zero is not allowed."
    return a / b
operations = {
    "+": add,
    "-" : subtract,
    "*" : multiply,
    "/" :divide
}
def calculator():
    print(logo)
    print("Welcome to the calculator!")
    should_continue = "y"
    num1 = float(input("what's the first number?: "))
    while should_continue == "y":
        operator = input("Pick an operation: +,-,*,/ : ")
        num2 = float(input("what's the second number?: "))
        if operator in operations:
            result = operations[operator](num1,num2)
            print(f"{num1} {operator} {num2} = {result}")
        should_continue = input("Do you want to continue with the result? (y/n): ")
        if should_continue == "y":
            num1 = result
        else:
            should_continue = "n"
            print("/n" * 8)
            calculator()
calculator()