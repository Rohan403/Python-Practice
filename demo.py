# For normally printing a message in same line
# print("Hello world","Hello Niladri Pal")
# Defining data types
# name = "Niladri"
# age = 26
# percentage = 99.5
# print(name,age,percentage)
# print(type(name))
# print(type(age))
# print(type(percentage))   # Here in python we do not need to define types it automatically detects.
# Inputs
# name = input("Enter your name: ")
# print("Hello",name)

# Practice Exercise
# Add a person as first name Tony and second name Stark, Tony's age is 53 and height is 1.53 metre take this superhero name as input and print it
# first_name = input("Enter first name: ")
# last_name = input("Enter last name: ")
# print(first_name+" "+last_name+"'s age is 53 and height is 1.53 metre")
# ----Type Conversion and Type casting----
# Type casting is the one which user converts the value while type conversion is which python automatically converts
# add = 1 + 3.5
# print(add) # This is type conversion
# print(int(add)) # This is type casting
# Know your age
# current_year = input("Enter current year: ")
# date_of_birth = input("Enter your DOB: ")
# age = int(current_year) - int(date_of_birth)
# print("Your age is:",age)

# Sum addition
# a = input("Enter first number: ")
# b = input("Enter second number: ")
# add = int(a) + int(b)
# print("Sum of 2 numbers is: ", add)

# Multiplication
# a = int(input("Enter first number: "))
# b = int(input("Enter second number: "))
# multiply = a * b
# print("Multiplication of 2 numbers is: ",multiply)

# String Operations
# name = "Niladri Pal"
# print(name.upper())
# print(name.lower())
# For finding the index of the we use find
# print(name.find("Pal"))
# For replacing we use replace
# print(name.replace("Niladri","Rohan"))
# in is default boolean in python that tells us if the character exists or not
# print("l" in name) # True
# print("z" in name) # False

# Problems
# Take inputs as 99.5,23.75 and 16.15 find the total bill and the average price

# first_price = float(input("Enter first price: "))
# second_price = float(input("Enter second price: "))
# third_price = float(input("Enter third price: "))
# total_price = first_price + second_price + third_price
# average_price = total_price / 3
# print("The total bill is",total_price,"and the average price is",average_price)

# Take a superhero name and as input and check if it starts with "S"/"s"
# name = input("Enter name: ")
# starts_with_s = name.lower().startswith('s')
# print(starts_with_s)

# Arithmetic operators
# print(5 + 5) #10
# print(5 - 2) #3
# print(5 * 2) #10
# print(5 / 3) #1.6666666666666667
# print(5 // 3) #1
# print(5 % 3) #2
# print(5 ** 3) #125

# Assignmentshortcuts

x = 5
x += 3 # x = x + 3
# print(x) # 8
# Similar shortcuts include:
# x -= 2
# x *= 3
# x /= 2
# x //= 2
# x %= 2
# x **= 2

# LogicalOperators
# Logical operators combine or reverse conditions.
# or
# Returns True when at least one condition is true:
# print((5 > 2) or (2 > 5)) # True
# and
# Returns True only when both conditions are true:
# print((5 > 2) and (2 > 5)) # False
# 13
# not
# Reverses a Boolean result:
# print(not (5 > 2)) # False

# Conditional statements

# age = 20

# Intendation
# if age >=18:
#     print("You can vote")
# else:
#     print("You cannot vote")

# Problem: Print students grade if student's mark is between 80-100 then 'A' grade, if 60-80 'B' if less than 60 then 'C'.

# marks = float(input("Enter student marks: "))

# if marks >= 80 and marks <= 100:
#     print("A")
# elif marks >= 60 and marks <= 80:
#     print("B")
# else:
#     print("C")
# range() Function
# range() generates a sequence of numbers, commonly used with loops.
# numbers = range(5)
# print(numbers)  # range(0, 5)
# # The general syntax is:
# # range(start, stop, step)
# # start is included.
# # stop is excluded.
# # step controls the difference between numbers.
# # The default start is 0
# # The default step is 1
# range(5) # 0, 1, 2, 3, 4
# range(1, 6)      # 1, 2, 3, 4, 5
# range(2, 11, 2)  # 2, 4, 6, 8, 10
# range(5, 0, -1)  # 5, 4, 3, 2, 1
# The stop value is not included in the sequence.
# While loops
# Print numbers
# counter = 1
# while counter <= 5:
#     print(counter)
#     counter += 1
# print("End of code")
# Print triangle
# i = 0
# while i <= 5:
#     print(i * "*")
#     i += 1
# Print numbers from 1 to 5 in decerasing format
# i = 5
# while i > 0:
#     print(i)
#     i -= 1
# Print an inverted triangle
# i = 5
# while i > 0:
# A while loop repeats a block of code while its condition is True
#     print(i * "*")
#     i -= 1
# For loops
# Print values from 0 to 4
# for i in range(5):
#     print(i)
# # Print values from 1 to 5
# for i in range(1,6):
#     print(i)
# Print values from 1 to 5 in decending order
# for i in range(5,0,-1):
#     print(i)
# Print even numbers using brute force
# for i in range(1,11):
#     if i % 2 == 0:
#         print(i)
# Print even numbers using range
# for i in range(2,11,2):
#     print(i)
# Problem using input print even numbers
# number = int(input("Enter a number: "))
# for i in range(2,number + 1,2):
#     print(i)
# Printing stars using for loop
# for i in range(1,6):
#     print(i * "*")
# Printing inverted stars
# for i in range(5,0,-1):
#     print(i * "*")
# Print all odd numbers from 1 to 20
# for i in range(1,21,2):
#     print(i)
# Print table of 57 using brute force
# for i in range(1,571):
#      if i % 57 == 0:
#       print(i)
# Print table of 57 using range
# for i in range (57,571,57):
#      print("57 x", i // 57, "=", i)
# Printing 57 table using table format
# for i in range(1,11):
#     print(57,"x",i,"=",57 * i)
# Print all the multiples of 3 from 1 to 50 but skip 15
# for i in range(3,51,3):
#     if i == 15:
#         continue
#     print(i)
# Take 2 numbers as input a and b, find and print the first number between 1 and 1000 that is divisible by both numbers;
# n1= int(input("Enter the first number: "))
# n2 = int(input("Enter the second number: "))
# for i in range(1,1001):
#     if i % n1 == 0 and i % n2 == 0:
#         print(i)
#         break