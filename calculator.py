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
    first_number = tokenized_input[1]
    second_number = tokenized_input[2]

    print(f"{operator}, {first_number}, {second_number}")
    
    # Declare result variable

    # Evaluate input, return correct operation