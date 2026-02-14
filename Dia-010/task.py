import art

def add(a,b):
    return a+b

def subtract(a,b):
    return a-b

def multiply(a,b):
    return a*b

def divide(a,b):
    if b==0:
        print("Number cannot be devided by zero")
        exit(0)
    return a/b

operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide
}

def calculator():
    should_accumulate = True

    print(art.logo)

    num1 = float(input("Type the first number: "))

    while should_accumulate:

        math_operator = input("Type a math operator(+, -, * or /): ")

        num2 = float(input("Type the second number: "))

        result = operations[math_operator](num1,num2)
        print(f"{num1} {math_operator} {num2} = {result:.2f}")
        choice = input("Do you want to continue? (y/n): ")
        if choice == 'y':
            num1 = result
        else:
            should_accumulate = False
            print("\n"*20)
            calculator()


calculator()