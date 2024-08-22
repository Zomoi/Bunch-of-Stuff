# printing a statement.
print("This is a statement!\n\n")

# storing data inside a variable and then using it to another print function.
name = input("What's your name? ") # input is actually a string function.
print(f"Hello there! {name}!") # what does f do? its a format string. 
print('Hey, %s!' %(name))# this is also valid.
print("Hello there! {}!\n\n".format(name)) # this is also another way. 

# arithmetic 
print("SECONDS IN DAYS!")
days = int(input("How many days? "))
days *= 24
days *= 60
days *= 60
print(f"Seconds in that many days : {days}\n\n")

# conditional statements
print("MAGNITUDE OF NUMBERS!")
number = int(input("Please type in a number: "))
if number < 1000 > 100:
    print("This number is smaller than 1000")
if number < 100 > 10:
    print("This number is smaller than 100")
if number < 10:
    print("This number is smaller than 10")

print ("Thank you!\n\n")

# boolean
print("CALCULATOR!")
num1 = int(input("Enter 1st number : "))
num2 = int(input("Enter 2nd number : "))
addition = num1+num2
subtraction = num1-num2
multiply = num1*num2
division = num1/num2
print("addition, subtraction, multiply, division")
operation = input("Please write one of the following operation you want the program to do: ")
if operation == "addition":
    print(f"{num1} + {num2} = {addition}")
elif operation == "subtraction":
    print(f"{num1} - {num2} = {subtraction}")
elif operation == "multiply":
    print(f"{num1} x {num2} = {multiply}")
elif operation == "division":
    print(f"{num1} / {num2} = {division}")

