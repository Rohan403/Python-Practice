# Calculator

first_number = float(input("Enter first number: "))
second_number = float(input("Enter second number: "))
operator = input("What operation do you want to perform? (+,-,/,*,%,**) ")

if operator == "+":
    print("Addition of two numbers are: ",first_number + second_number)
elif operator == "-":
    print("Subtraction of two numbers are: ", first_number - second_number)
elif operator == "*":
    print("Multiplication of two numbers are: ", first_number * second_number)
elif operator == "/":
    print("Division of two numbers are: ", first_number / second_number)
elif operator == "%":
    print("Module of two numbers are: ", first_number % second_number)
elif operator == "**":
    print("Asterics of two numbers are: ", first_number ** second_number)
else:
    print("Please enter a valid input")