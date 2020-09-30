"""CLI application for a prefix-notation calculator."""

from arithmetic import (add, subtract, multiply, divide, square, cube,
                        power, mod, )

# While statement
while True:
    # Capture user input
    user_input = input("Enter your equation> ")

    # Tokenize input
    tokenized_input = user_input.split(" ")

    # Check if first token is "q"
    if tokenized_input[0] == "q":
        break
    # Assign individual tokens to variables
    operator = tokenized_input[0]
    num1 = float(tokenized_input[1])
    num2 = float(tokenized_input[2])

    print(f"{operator}, {num1}, {num2}")

    # Declare result variable
    result = None

    # Evaluate input, return correct operation
    if operator == "+":
        result = add(num1, num2)
  
    print(result)