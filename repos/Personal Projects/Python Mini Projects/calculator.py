def multiply(a, b):
    return a * b

def divide(a, b):
    return a /b

def modulus(a, b):
    return a % b

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b 

operations = {
    "*": multiply,
    "/": divide,
    "%": modulus,
    "+": add,
    "-": subtract,
}

def calculate(operation, a, b):
    function = operations.get(operation)
    # checks if function is not None
    if function:
        return function(a, b)
    else:
        return ("Could not perform calculation.")

def main(): 
    # removes any white space after the input
    equation = input("Enter your equation here: ").strip()
    parts = equation.split()

    if len(parts) != 3:
        print("Incorrect format. Please try again.")

    numOne = int(parts[0])
    numTwo = int(parts[2])
    operation = (parts[1])
    answer = calculate(operation, numOne, numTwo)

    print(f"The result of {numOne} {operation} {numTwo} is: {answer}")

while True: 
    print("Hello! Welcome to the calculator app ^_^")
    print("Please enter you equation in the format once prompted: 4 * 2")
    print("You may use one of the five operations [* / % + -]")
    main() 
    playAgain = input("Exit calculator (Y/N)?").strip().upper() 
    if playAgain == "Y":
        break
    elif playAgain == "N": 
        continue
    else:
        print("Invalid input. Please enter 'Y' or 'N'") 


